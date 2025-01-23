#!/usr/bin/env python3
import dotenv
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.errors import SlackApiError

dotenv.load_dotenv()

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("BOT_USER_OAUTH_TOKEN"))

@app.message()
def message_received(args, message):
  if "ligma" in message["text"]:
    args.say(f"Ligma balls <@{message['user']}>")
  else:
    if "pog" in message["text"]:
      args.client.reactions_add(
        channel=message["channel"],
        thread_ts=message.get("thread_ts"),
        timestamp=message["ts"],
        name="marypog",
      )
    # We must do this if nothing else just to say we got the message!
    # (args.say is special and will do it for us)
    args.ack()

@app.event("reaction_added")
def on_reaction(args, event):
  # We're only interested in pog reacts to messages
  if event["item"]["type"] != "message" or event["reaction"] != "marypog":
    args.ack()
    return

  # Add a reaction of our own to that message
  try:
    args.client.reactions_add(
      channel=event["item"]["channel"],
      thread_ts=event["item"].get("thread_ts"),
      timestamp=event["item"]["ts"],
      name="marypog",
    )
  except SlackApiError as err:
    # If we have a reaction on this message already, slack will yet at us.
    # Ignore it:
    if err.response.data["error"] != "already_reacted":
      raise err

  # Must acknowledge
  args.ack()

@app.event("reaction_removed")
def on_reaction_removed(args, event):
  # Must acknowledge
  args.ack()


# Start your app
if __name__ == "__main__":
  SocketModeHandler(app, os.environ["APP_LEVEL_TOKEN"]).start()
