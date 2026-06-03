@echo off
:: Remove old task if it exists
powershell.exe -ExecutionPolicy Bypass -Command "Unregister-ScheduledTask -TaskName 'Business Brain Notion Meeting Pull' -Confirm:$false -ErrorAction SilentlyContinue"

:: Create new task -- daily at 4:00 PM
powershell.exe -ExecutionPolicy Bypass -Command "$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-WindowStyle Hidden -ExecutionPolicy Bypass -File \"C:\Users\joshu\Documents\Business_Brain\notion-meetings-pull.ps1\"'; $trigger = New-ScheduledTaskTrigger -Daily -At '16:00'; $settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Hours 1) -RunOnlyIfNetworkAvailable; $principal = New-ScheduledTaskPrincipal -UserId 'joshu' -LogonType Interactive; Register-ScheduledTask -TaskName 'Business Brain Notion Meeting Pull' -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Force"
echo Done. Notion meeting pull task registered for 4:00 PM daily.
