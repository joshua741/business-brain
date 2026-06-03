"""Dry-run-gated, allowlisted payment send path for the Mercury disbursement hub.

This is the safety layer between "AI decides a payment is due" and "money actually
leaves the account." Two guarantees:
  1. build_payment_set() refuses any recipient not on the allowlist.
  2. send_payments() does NOTHING unless confirm=True is explicitly passed.
"""


class UnlistedRecipientError(Exception):
    """Raised when an obligation targets a recipient not on the approved allowlist."""
    pass


def build_payment_set(obligations, allowlist):
    """Turn obligations into a validated payment set.

    obligations: list of {recipient, amount, from_account, memo}.
    allowlist:   set/collection of approved recipient names.
    Raises UnlistedRecipientError on the first recipient not in the allowlist.
    """
    payments = []
    for ob in obligations:
        if ob["recipient"] not in allowlist:
            raise UnlistedRecipientError(ob["recipient"])
        payments.append({
            "recipient": ob["recipient"],
            "amount": round(ob["amount"], 2),
            "from_account": ob["from_account"],
            "memo": ob["memo"],
        })
    return payments


def send_payments(payment_set, send_fn, confirm=False):
    """Dry-run by default. Calls send_fn (the real Mercury API call) only when confirm=True.

    Returns a report list mirroring payment_set with a `sent` flag, so a dry-run
    can be shown for approval before anything moves.
    """
    report = []
    for p in payment_set:
        if confirm:
            send_fn(p)
        report.append({**p, "sent": bool(confirm)})
    return report
