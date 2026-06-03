@echo off
echo Opening Google sign-in in your browser...
echo Pick your account and click ALLOW. This window will say "Credentials saved" when done.
echo.
gcloud auth application-default login --scopes=https://www.googleapis.com/auth/spreadsheets.readonly,https://www.googleapis.com/auth/drive.readonly,https://www.googleapis.com/auth/cloud-platform
echo.
echo ====================================================
echo If you see "Credentials saved" above, you're done.
echo You can close this window and tell Claude "done".
echo ====================================================
pause
