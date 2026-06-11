"""
Run this locally ONCE per Gmail account to get a refresh token.
Then set the token as an env var in Railway.

Usage:
  pip install google-auth-oauthlib
  python auth_setup.py
"""
from google_auth_oauthlib.flow import InstalledAppFlow

def main():
    print("Gmail MCP Auth Setup")
    print("--------------------")
    client_id = input("Google Client ID: ").strip()
    client_secret = input("Google Client Secret: ").strip()
    account = input("Account label (e.g. joshua or docs): ").strip().upper()

    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost:8080"],
        }
    }

    flow = InstalledAppFlow.from_client_config(
        client_config,
        scopes=["https://mail.google.com/"],
        redirect_uri="http://localhost:8080",
    )

    print("\nA browser window will open. Sign in with the correct Gmail account and grant all permissions.")
    creds = flow.run_local_server(port=8080, access_type="offline", prompt="consent")

    print("\n========================================")
    print("Add this to Railway environment variables:")
    print(f"{account}_GMAIL_REFRESH_TOKEN={creds.refresh_token}")
    print("========================================\n")


if __name__ == "__main__":
    main()
