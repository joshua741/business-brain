import pytest
from payments import build_payment_set, send_payments, UnlistedRecipientError

ALLOWLIST = {"Dillon Ford", "Shelby McDonald"}


def test_builds_per_obligation_payments():
    obligations = [
        {"recipient": "Dillon Ford", "amount": 2310.94, "from_account": "1312-operating", "memo": "1312 65th Dr seller finance"},
        {"recipient": "Shelby McDonald", "amount": 1800.00, "from_account": "2102-rehab", "memo": "2102 68th St draw"},
    ]
    payments = build_payment_set(obligations, ALLOWLIST)
    assert len(payments) == 2
    assert payments[0]["memo"] == "1312 65th Dr seller finance"
    assert payments[0]["from_account"] == "1312-operating"


def test_unlisted_recipient_blocked():
    obligations = [{"recipient": "Unknown LLC", "amount": 500, "from_account": "hub", "memo": "x"}]
    with pytest.raises(UnlistedRecipientError):
        build_payment_set(obligations, ALLOWLIST)


def test_dry_run_does_not_send():
    sent = []
    payments = [{"recipient": "Dillon Ford", "amount": 2310.94, "from_account": "hub", "memo": "x"}]
    report = send_payments(payments, send_fn=lambda p: sent.append(p), confirm=False)
    assert sent == []
    assert report[0]["sent"] is False


def test_confirm_sends():
    sent = []
    payments = [{"recipient": "Dillon Ford", "amount": 2310.94, "from_account": "hub", "memo": "x"}]
    report = send_payments(payments, send_fn=lambda p: sent.append(p), confirm=True)
    assert len(sent) == 1
    assert report[0]["sent"] is True
