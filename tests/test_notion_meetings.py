import sys, pathlib, tempfile, os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "connectors"))
import notion_meetings as nm


def test_parse_env():
    with tempfile.TemporaryDirectory() as d:
        env = pathlib.Path(d) / ".env"
        env.write_text(
            "# a comment\n"
            "NOTION_API_KEY=ntn_abc123\n"
            "\n"
            'NOTION_MEETINGS_DB_ID="db-id-456"\n'
            "EXPORT_NOTE=export ignored=here\n",
            encoding="utf-8",
        )
        cfg = nm.parse_env(env)
        assert cfg["NOTION_API_KEY"] == "ntn_abc123", cfg
        assert cfg["NOTION_MEETINGS_DB_ID"] == "db-id-456", cfg  # quotes stripped
        assert cfg["EXPORT_NOTE"] == "export ignored=here", cfg  # only first = splits
        # missing file -> empty
        assert nm.parse_env(pathlib.Path(d) / "nope.env") == {}


def test_rich_text():
    rt = [{"plain_text": "Hello "}, {"plain_text": "world"}]
    assert nm.rich_text_to_str(rt) == "Hello world"
    assert nm.rich_text_to_str(None) == ""


def test_blocks_to_markdown():
    blocks = [
        {"type": "heading_1", "heading_1": {"rich_text": [{"plain_text": "Summary"}]}},
        {"type": "paragraph", "paragraph": {"rich_text": [{"plain_text": "We met."}]}},
        {"type": "bulleted_list_item",
         "bulleted_list_item": {"rich_text": [{"plain_text": "point a"}]}},
        {"type": "to_do",
         "to_do": {"rich_text": [{"plain_text": "ship it"}], "checked": True}},
        {"type": "divider", "divider": {}},
    ]
    md = nm.blocks_to_markdown(blocks)
    assert "# Summary" in md, md
    assert "We met." in md, md
    assert "- point a" in md, md
    assert "- [x] ship it" in md, md
    assert "---" in md, md


def test_blocks_recurse():
    blocks = [{
        "type": "toggle",
        "toggle": {"rich_text": [{"plain_text": "Transcript"}]},
        "children": [
            {"type": "paragraph",
             "paragraph": {"rich_text": [{"plain_text": "Mostafa: hi"}]}},
        ],
    }]
    md = nm.blocks_to_markdown(blocks)
    assert "Transcript" in md, md
    assert "Mostafa: hi" in md, md


def test_is_meeting_title():
    assert nm.is_meeting_title("Morning Meeting Josh & Mostafa 2026-06-02T12:00:00.000-05:00")
    assert nm.is_meeting_title("Video Call with Yvonne and Josh 2026-05-30T14:30:00.000-05:00")
    assert nm.is_meeting_title("Weekly Role Play w/ Jon")
    assert nm.is_meeting_title("2026-05-19T09:02:00.000-05:00")  # bare timestamp recording
    # non-meeting pages excluded
    assert not nm.is_meeting_title("Joshua Webber - Business Master Prompt")
    assert not nm.is_meeting_title("LLM Wiki (Personal)")
    assert not nm.is_meeting_title("+18067244064")  # Vince SMS conversation
    assert not nm.is_meeting_title("Meeting Transcripts")  # the container page itself
    assert not nm.is_meeting_title("")


def test_slug_from_title():
    assert nm.slug_from_title(
        "Morning Meeting Josh & Mostafa 2026-06-02T12:00:00.000-05:00"
    ) == "morning-meeting-josh-mostafa"
    assert nm.slug_from_title("2026-05-19T09:02:00.000-05:00") == "meeting"  # stamp stripped


def test_page_title():
    page = {"properties": {"Name": {"type": "title",
            "title": [{"plain_text": "Morning Meeting"}]}}}
    assert nm.page_title(page) == "Morning Meeting"


def test_target_name():
    assert nm.target_name("2026-06-03", "morning-meeting", set()) == \
        "transcript-2026-06-03-morning-meeting.md"
    existing = {"transcript-2026-06-03-morning-meeting.md"}
    assert nm.target_name("2026-06-03", "morning-meeting", existing) == \
        "transcript-2026-06-03-morning-meeting-2.md"


def test_page_date_from_title():
    page = {"properties": {"Name": {"type": "title", "title": [
        {"plain_text": "Morning Meeting Josh & Mostafa 2026-06-02T12:00:00.000-05:00"}]}},
        "created_time": "2026-01-01T00:00:00.000Z"}
    assert nm.page_date(page) == "2026-06-02"  # date pulled from title, not created_time


def test_needs_ingest():
    manifest = {"page1": {"last_edited_time": "2026-06-03T10:00:00.000Z"}}
    assert nm.needs_ingest("page1", "2026-06-03T10:00:00.000Z", manifest) is False  # unchanged
    assert nm.needs_ingest("page1", "2026-06-03T11:00:00.000Z", manifest) is True   # edited
    assert nm.needs_ingest("page2", "2026-06-03T09:00:00.000Z", manifest) is True   # new


def test_with_retries_succeeds():
    calls = {"n": 0}

    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise nm.TransientAPIError("429")
        return "ok"

    slept = []
    assert nm.with_retries(flaky, sleeper=slept.append, attempts=5) == "ok"
    assert calls["n"] == 3
    assert len(slept) == 2


def test_with_retries_gives_up():
    def always_fail():
        raise nm.TransientAPIError("500")

    slept = []
    raised = False
    try:
        nm.with_retries(always_fail, sleeper=slept.append, attempts=3)
    except nm.TransientAPIError:
        raised = True
    assert raised
    assert len(slept) == 2  # slept between attempts, not after the last


def test_page_date():
    page = {"properties": {"Date": {"date": {"start": "2026-06-03"}}},
            "created_time": "2026-01-01T00:00:00.000Z"}
    assert nm.page_date(page) == "2026-06-03"
    # falls back to created_time when no Date property value
    page2 = {"properties": {"Date": {"date": None}},
             "created_time": "2026-05-30T12:00:00.000Z"}
    assert nm.page_date(page2) == "2026-05-30"


def run():
    test_parse_env()
    test_rich_text()
    test_blocks_to_markdown()
    test_blocks_recurse()
    test_is_meeting_title()
    test_slug_from_title()
    test_page_title()
    test_target_name()
    test_needs_ingest()
    test_with_retries_succeeds()
    test_with_retries_gives_up()
    test_page_date()
    test_page_date_from_title()
    print("test_notion_meetings PASS")


if __name__ == "__main__":
    run()
