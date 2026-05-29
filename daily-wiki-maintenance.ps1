# Business Brain — Daily Wiki Maintenance
# Runs at 6:57 AM via Windows Task Scheduler

$repoPath = "C:\Users\joshu\Documents\Business_Brain"
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

# 1. Pull latest
Log "git pull"
& $git pull origin master 2>&1 | ForEach-Object { Log $_ }

# 2. Run Claude wiki maintenance
Log "Running Claude lint agent"
$prompt = @"
You are the daily maintenance agent for Joshua Webber's Business Brain wiki stored in the current directory.

Do the following silently:

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
4. Append to wiki/log.md: ## [$date] lint | [one-line summary of what was fixed]
5. Write $date to wiki/.last-ingest

Do not run any git commands. Exit when done.
"@

& $claude --print $prompt --dangerously-skip-permissions 2>&1 | ForEach-Object { Log $_ }

# 3. Commit and push if anything changed
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
