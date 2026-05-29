@echo off
powershell.exe -ExecutionPolicy Bypass -Command "$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-WindowStyle Hidden -ExecutionPolicy Bypass -File \"C:\Users\joshu\.claude\Business_Brain\daily-wiki-maintenance.ps1\"'; $trigger = New-ScheduledTaskTrigger -Daily -At '06:57'; $settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Hours 1) -RunOnlyIfNetworkAvailable; $principal = New-ScheduledTaskPrincipal -UserId 'joshu' -LogonType Interactive -RunLevel Highest; Register-ScheduledTask -TaskName 'Business Brain Daily Wiki Maintenance' -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Force"
echo Done. Task registered.
pause
