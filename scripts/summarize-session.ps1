# Summarize the just-ended Claude session and write to raw/
# Called by the Stop hook in settings.json
#
# The Stop hook fires on EVERY assistant turn, not once per session. Without a
# throttle this produces dozens of files per day. Guards below ensure we write
# at most one memo per THROTTLE_MINUTES window, only when the session has real
# substance, and never write an empty/failed file.

$repoPath  = "C:\Users\joshu\Documents\Business_Brain"
$rawPath   = "$repoPath\raw"
$claude    = "C:\Users\joshu\AppData\Roaming\npm\claude.cmd"
$date      = Get-Date -Format "yyyy-MM-dd"
$timestamp = Get-Date -Format "yyyy-MM-ddTHH-mm-ss"
$outFile   = "$rawPath\memo-$timestamp-session.md"

$THROTTLE_MINUTES = 30   # collapse a session's many turns into ~one memo per window
$MIN_EXCHANGES    = 8    # skip trivial sessions
$MIN_MEMO_CHARS   = 200  # skip empty/failed model output

# --- Throttle: if a memo was written recently, skip this turn entirely ---
$recent = Get-ChildItem -Path $rawPath -Filter "memo-*-session.md" -ErrorAction SilentlyContinue |
          Sort-Object LastWriteTime -Descending |
          Select-Object -First 1
if ($recent -and (New-TimeSpan -Start $recent.LastWriteTime).TotalMinutes -lt $THROTTLE_MINUTES) {
    exit 0
}

# --- Find the most recent session transcript ---
$transcriptDir = "C:\Users\joshu\.claude\projects"
$latest = Get-ChildItem -Path $transcriptDir -Filter "*.jsonl" -Recurse -ErrorAction SilentlyContinue |
          Sort-Object LastWriteTime -Descending |
          Select-Object -First 1
if (-not $latest) { exit 0 }

# --- Extract readable messages from the transcript ---
$messages = Get-Content $latest.FullName |
    ForEach-Object { $_ | ConvertFrom-Json -ErrorAction SilentlyContinue } |
    Where-Object { $_.type -eq "user" -or $_.type -eq "assistant" } |
    ForEach-Object {
        $role = $_.type.ToUpper()
        $content = if ($_.message.content -is [string]) { $_.message.content }
                   elseif ($_.message.content) { ($_.message.content | Where-Object { $_.type -eq "text" } | Select-Object -First 1).text }
                   else { "" }
        if ($content) { "$role`: $content" }
    } |
    Select-Object -Last 60  # last 60 exchanges

# Skip trivial sessions
if (-not $messages -or $messages.Count -lt $MIN_EXCHANGES) { exit 0 }

$transcript = $messages -join "`n`n"

$prompt = @"
You are summarizing a Claude Code session for Joshua Webber's Business Brain wiki.

Transcript (last portion):
$transcript

Write a concise memo in this exact format. If the session contained no business/personal
substance worth preserving (e.g. it was only debugging, setup, or chit-chat), output the
single token SKIP and nothing else.

---
name: memo-$timestamp-session
type: source
tags: [session, memo]
sources: [auto-generated]
updated: $date
---

# Session Memo — $date

**Summary**: [2-3 sentence summary of what was discussed or accomplished]

**Key decisions**: [bullet list of decisions made, if any]

**Business context captured**: [bullet list of new facts about Joshua's business, preferences, or projects — only non-obvious things worth preserving]

**Action items**: [bullet list of next steps or open items, if any]

**Related wiki pages**: [list of wiki pages this session touches, e.g. [[lbk-cleaners]], [[vince-ai]]]

Only include sections with actual content. Skip empty sections.
"@

# Capture output to a variable FIRST — only write a file if it is real content.
$result = (& $claude --print $prompt --dangerously-skip-permissions 2>&1 | Out-String).Trim()

if ($result.Length -lt $MIN_MEMO_CHARS -or $result -match '^\s*SKIP\s*$') {
    exit 0
}

Set-Content -Path $outFile -Value $result -Encoding utf8
