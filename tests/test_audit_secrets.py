import sys, pathlib, tempfile
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "lib"))
from audit_secrets import scan

def run():
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        (root / "raw").mkdir()
        (root / "wiki").mkdir()
        # planted unmasked secrets
        (root / "raw" / "a.md").write_text("SSN 123-45-6789 and acct 4000015856987", encoding="utf-8")
        # clean / already-masked content
        (root / "wiki" / "b.md").write_text("amount $2,310.94 EIN 39-2122418 acct 20XXXXXX6030", encoding="utf-8")
        hits = scan(root)
        joined = " ".join(hits)
        assert any("a.md" in h for h in hits), hits
        assert "123-45-6789" in joined, hits
        assert "4000015856987" in joined, hits
        # clean file must not be flagged
        assert not any("b.md" in h for h in hits), hits
    print("test_audit_secrets PASS")

if __name__ == "__main__":
    run()
