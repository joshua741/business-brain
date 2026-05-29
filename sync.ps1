# Business Brain daily sync — pulls latest wiki + CLAUDE.md from GitHub
Set-Location "C:\Users\joshu\.claude\Business_Brain"
git pull origin master 2>&1 | Out-Null

# If repo has an updated CLAUDE.md, copy it to the session location
$repoClaude = "C:\Users\joshu\.claude\Business_Brain\CLAUDE.md"
$sessionClaude = "C:\Users\joshu\CLAUDE.md"
if (Test-Path $repoClaude) {
    $repoContent = Get-Content $repoClaude -Raw
    $sessionContent = Get-Content $sessionClaude -Raw
    if ($repoContent -ne $sessionContent) {
        Copy-Item $repoClaude $sessionClaude -Force
    }
}
