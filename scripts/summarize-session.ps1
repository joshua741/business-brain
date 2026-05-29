# Summarize the just-ended Claude session and write to raw/
# Called by the Stop hook in settings.json

$repoPath  = "C:\Users\joshu\Documents\Business_Brain"
$rawPath   = "$repoPath\raw"
$claude    = "C:\Users\joshu\AppData\Roaming\npm\claude.cmd"
$date      = Get-Date -Format "yyyy-MM-dd"
$timestamp = Get-Date -Format "yyyy-MM-ddTHH-mm-ss"
$outFile   = "$rawPath\memo-$timestamp-session.md"

# Find the most recent session transcript
$transcriptDir = "C:\Users\joshu\.claude\projects"
$latest = Get-ChildItem -Path $transcriptDir -Filter "*.jsonl" -Recurse |
          Sort-Object LastWriteTime -Descending |
          Select-Object -First 1

if (-not $latest) { exit 0 }

# Extract readable messages from the transcript
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

if (-not $messages) { exit 0 }

$transcript = $messages -join "`n`n"

$prompt = @"
You are summarizing a Claude Code session for Joshua Webber's Business Brain wiki.

Transcript (last portion):
$transcript

Write a concise memo in this exact format:

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

& $claude --print $prompt --dangerously-skip-permissions | Out-File -FilePath $outFile -Encoding utf8
