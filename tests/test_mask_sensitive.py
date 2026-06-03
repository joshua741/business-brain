import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "lib"))
from mask_sensitive import mask_text

def run():
    # SSN masked to last 4
    assert mask_text("SSN 123-45-6789 on file") == "SSN XXX-XX-6789 on file"
    # bare account/loan digit-run (>=8) masked: keep first 2 + last 4
    assert mask_text("Account 200012346030 active") == "Account 20XXXXXX6030 active"
    # card number masked
    assert mask_text("Card 4111111111111111") == "Card 41XXXXXXXXXX1111"
    # dollar amounts preserved
    assert mask_text("Mortgage $2,310.94/mo") == "Mortgage $2,310.94/mo"
    # entity EIN preserved (NN-NNNNNNN)
    assert mask_text("EIN 39-2122418") == "EIN 39-2122418"
    # ISO dates preserved
    assert mask_text("closed 2026-06-03") == "closed 2026-06-03"
    # already-masked values left alone (contain X, not pure digits)
    assert mask_text("acct 20XXXXXX6030") == "acct 20XXXXXX6030"
    print("test_mask_sensitive PASS")

if __name__ == "__main__":
    run()
