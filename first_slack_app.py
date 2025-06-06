#!/usr/bin/env python3
import dotenv
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.errors import SlackApiError
import biblePython
import biblePython.checkMessage

dotenv.load_dotenv()

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("BOT_USER_OAUTH_TOKEN"))

@app.message()
def message_received(args, message):
  thread_ts=message.get("thread_ts")
  if thread_ts and any(sub in message["text"] for sub in biblePython.checkMessage.QUESTIONS) :
    thread_ts=message.get("thread_ts")
    channel_id = message.get("channel", "")
    if channel_id != "C06HLL9CL": # botspam channel
      quit
    respond_to = args.client.conversations_replies(channel=channel_id, ts=thread_ts)[0]
    response = biblePython.checkMessage.generate_response(respond_to)
    args.say(response)
    # We must do this if nothing else just to say we got the message!
    # (args.say is special and will do it for us)
    args.ack()

# @app.event("reaction_added")
# def on_reaction(args, event):
#   # We're only interested in pog reacts to messages
#   if event["item"]["type"] != "message" or event["reaction"] != "marypog":
#     args.ack()
#     return

#   # Add a reaction of our own to that message
#   try:
#     args.client.reactions_add(
#       channel=event["item"]["channel"],
#       thread_ts=event["item"].get("thread_ts"),
#       timestamp=event["item"]["ts"],
#       name="marypog",
#     )
#   except SlackApiError as err:
#     # If we have a reaction on this message already, slack will yet at us.
#     # Ignore it:
#     if err.response.data["error"] != "already_reacted":
#       raise err

#   # Must acknowledge
#   args.ack()

# @app.event("reaction_removed")
# def on_reaction_removed(args, event):
#   # Must acknowledge
#   args.ack()


# # Start your app
# if __name__ == "__main__":
#   SocketModeHandler(app, os.environ["APP_LEVEL_TOKEN"]).start()
