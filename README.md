# Your First Slack Bot!

Making a basic slack bot with Bolt and Python.

## Getting credentials
* Clone this repo
  * `git clone https://github.com/Mstrodl/your-first-slack-bot`
  * Copy `.env.sample` to `.env`
* Creating the application
  * Go to https://api.slack.com/apps
  * Click "Create New App"
  * When prompted, paste this manifest:
```json
{
  "display_information": {
    "name": "My First Slack Bot"
  },
  "features": {
    "bot_user": {
      "display_name": "My First Slack Bot",
      "always_online": false
    }
  },
  "oauth_config": {
    "scopes": {
      "bot": [
        "channels:history",
        "chat:write",
        "groups:history",
        "reactions:read",
        "reactions:write",
        "users:read"
      ]
    }
  },
  "settings": {
    "event_subscriptions": {
      "bot_events": ["message.channels", "reaction_added", "reaction_removed"]
    },
    "interactivity": {
      "is_enabled": true
    },
    "org_deploy_enabled": false,
    "socket_mode_enabled": true,
    "token_rotation_enabled": false
  }
}
```
* Create an app-level token
  * Under the "Basic Information" tab in your new application, click "Generate Tokens and Scopes" under "App-Level Tokens"
  * Add the scope `connections:write`
  * Set "Token Name" to `bolt`
  * Save
  * the token and save it to the `.env` file in this repo (`APP_LEVEL_TOKEN=xapp-...`)
  * Press Done
* Create an oauth token
  * Go to the "OAuth & Permissions"
  * Click "Install to Workspace Name Here"
  * After your app is installed, this tab will have a "Bot User OAuth Token" field
  * Copy the "Bot User OAuth Token" field into your `.env` file: `BOT_USER_OAUTH_TOKEN=xoxb-...`

## Setting up the development environment

* Run `python3 -m venv venv` to create a virtual environment
* Run `. ./venv/bin/activate` to start the virtual environment
* Run `pip install -r requirements.txt`
* Run `./app.py` to start!
