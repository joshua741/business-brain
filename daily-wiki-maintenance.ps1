# Business Brain -- Daily Wiki Maintenance
# Runs at 6:57 AM via Windows Task Scheduler
# Sequence: git pull  download Drive briefings  ingest  lint  commit  push

$repoPath = "C:\Users\joshu\Documents\Business_Brain"
$rawPath  = "$repoPath\raw"
$logFile  = "$repoPath\daily-maintenance.log"
$claude   = "C:\Users\joshu\AppData\Roaming\npm\claude.cmd"
$git      = "C:\Program Files\Git\cmd\git.exe"
$gh       = "C:\Program Files\GitHub CLI\gh.exe"
$date     = Get-Date -Format "yyyy-MM-dd"

function Log($msg) {
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "[$ts] $msg" | Out-File -Append -Encoding utf8 $logFile
}

Set-Location $repoPath
$env:BB_CAPTURE_RUNNING = "1"  # suppress session-capture hooks during the automated run
Log "=== Daily maintenance started ==="

# 1. Pull latest from GitHub
Log "git pull"
& $git pull origin master 2>&1 | ForEach-Object { Log $_ }

# 2. Download today's briefing files from Google Drive into raw/
Log "Downloading briefings from Google Drive"
$downloadPrompt = @"
Check Google Drive for a folder named 'Business Brain Briefings'.
Find any files in that folder with today's date ($date) in the filename that have not already been copied to the raw/ directory.
For each new file found, download its content and write it as a .md file in the raw/ directory of the current working directory.
Name each file exactly as it appears in Google Drive.
If no new files exist for today, output: NO_NEW_FILES
Otherwise output: DOWNLOADED [comma-separated list of filenames]
"@
& $claude --print $downloadPrompt --dangerously-skip-permissions 2>&1 | ForEach-Object { Log $_ }

# 2b. Local-files connector: convert drop-folder docs (pdf/csv/xlsx/md) into masked raw/ .md
Log "Local-files connector (drop folder)"
& python "$repoPath\connectors\local_files.py" 2>&1 | ForEach-Object { Log $_ }

# 2b2. GHL connector (read-only daily snapshot; self-skips if creds absent)
Log "GHL connector"
& python "$repoPath\connectors\ghl.py" 2>&1 | ForEach-Object { Log $_ }

# 2b3. Twilio connector (read-only SMS log snapshot; self-skips if creds absent)
Log "Twilio connector"
& python "$repoPath\connectors\twilio_logs.py" 2>&1 | ForEach-Object { Log $_ }

# 2c. Connector discovery / gap detector -> connectors/STATUS.md
Log "Connector gap detector"
& python "$repoPath\connectors\discover_gaps.py" 2>&1 | ForEach-Object { Log $_ }

# 3. Run Claude wiki ingest + lint
Log "Running wiki ingest and lint agent"
$maintPrompt = @"
You are the daily maintenance agent for Joshua Webber's Business Brain wiki stored in the current directory ($repoPath).

CRITICAL: You are running fully autonomous with NO human present. Nobody can answer questions or approve anything. Do NOT ask questions. Do NOT produce a report and wait for approval. Directly CREATE and EDIT the files yourself with your file tools. Make your best judgment on any uncertainty and proceed. Your ONLY chat output should be a one-line summary at the very end.

Skip any source file that is empty (0 bytes) or contains no meaningful content -- do not create a page for it.

Do the following in order:

1. Read wiki/.last-ingest for reference only (do NOT use it as a filter).
2. INGEST BY RECONCILIATION (not by date). For every file in raw/ (recursively, *.md), determine whether a wiki/source-*.md page already lists that exact filename in its `sources:` frontmatter. For each raw file with NO such source page, ingest it now:
   - Create a source page in wiki/ named source-[kebab-title].md (frontmatter: name, type: source, tags, sources: [<exact raw filename>], updated: $date) with a detailed summary including specific figures, dates, parties, (source: <filename>) citations, and [[wikilinks]]
   - Create or update entity, project, concept, and person pages it touches
   - Add wikilinks throughout
   - Add the source to wiki/index.md under Sources
   - APP ROUTING: if the source is relevant to the wih-app CRM (CRM features, AI agents, dashboards, automations, or any of the three verticals: wholesale/creative finance, property management, capital raising), also append a one-line idea with a [[wikilink]] to the "Feature context to fold in" section of wiki/wih-app.md.
3. Run wiki lint:
   - Orphan pages: find pages with no inbound wikilinks, add a link from the most relevant page
   - Missing pages: find [[wikilinks]] with no corresponding file, create stub pages with correct frontmatter
   - Contradictions: flag in wiki/log.md, do not auto-resolve
   - Stale status: update status fields where evidence supports it
4. Append to wiki/log.md: ## [$date] lint | [one-line summary of what was fixed/ingested]
5. Write $date to wiki/.last-ingest

Do not run any git commands. Exit when done.
"@
& $claude --print $maintPrompt --dangerously-skip-permissions 2>&1 | ForEach-Object { Log $_ }

# 3b. Privacy gate -- audit for unmasked secrets (warning) + hard repo-private check
Log "Secret audit (non-fatal warning)"
& python "$repoPath\lib\audit_secrets.py" 2>&1 | ForEach-Object { Log $_ }

Log "Repo visibility check"
$isPrivate = (& $gh repo view joshua741/business-brain --json isPrivate -q .isPrivate 2>&1 | Out-String).Trim()
Log "isPrivate=$isPrivate"
if ($isPrivate -ne 'true') {
    Log "ABORT: repo is NOT private -- refusing to commit/push sensitive data."
    Log "=== Daily maintenance halted on privacy gate ==="
    exit 1
}

# 4. Commit and push if anything changed
$changes = & $git status --porcelain 2>&1
if ($changes) {
    Log "Changes detected -- committing"
    & $git add -A 2>&1 | ForEach-Object { Log $_ }
    & $git commit -m "chore: daily wiki maintenance $date" 2>&1 | ForEach-Object { Log $_ }
    & $git push origin master 2>&1 | ForEach-Object { Log $_ }
    Log "Pushed to GitHub"
} else {
    Log "No changes -- nothing to commit"
}

Log "=== Daily maintenance complete ==="
