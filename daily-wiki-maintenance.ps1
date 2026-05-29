# Business Brain — Daily Wiki Maintenance
# Runs at 6:57 AM via Windows Task Scheduler
# Sequence: git pull → download Drive briefings → ingest → lint → commit → push

$repoPath = "C:\Users\joshu\Documents\Business_Brain"
$rawPath  = "$repoPath\raw"
$logFile  = "$repoPath\daily-maintenance.log"
$claude   = "C:\Users\joshu\AppData\Roaming\npm\claude.cmd"
$git      = "C:\Program Files\Git\cmd\git.exe"
$date     = Get-Date -Format "yyyy-MM-dd"

function Log($msg) {
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "[$ts] $msg" | Out-File -Append -Encoding utf8 $logFile
}

Set-Location $repoPath
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

# 3. Run Claude wiki ingest + lint
Log "Running wiki ingest and lint agent"
$maintPrompt = @"
You are the daily maintenance agent for Joshua Webber's Business Brain wiki stored in the current directory ($repoPath).

Do the following in order:

1. Read wiki/.last-ingest to get the last ingest timestamp.
2. List all files in raw/. For any file newer than .last-ingest, auto-ingest it:
   - Create a source page in wiki/ named source-[kebab-title].md
   - Create or update entity, project, concept, and person pages it touches
   - Add wikilinks throughout
   - Add the source to wiki/index.md under Sources
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

# 4. Commit and push if anything changed
$changes = & $git status --porcelain 2>&1
if ($changes) {
    Log "Changes detected — committing"
    & $git add -A 2>&1 | ForEach-Object { Log $_ }
    & $git commit -m "chore: daily wiki maintenance $date" 2>&1 | ForEach-Object { Log $_ }
    & $git push origin master 2>&1 | ForEach-Object { Log $_ }
    Log "Pushed to GitHub"
} else {
    Log "No changes — nothing to commit"
}

Log "=== Daily maintenance complete ==="
