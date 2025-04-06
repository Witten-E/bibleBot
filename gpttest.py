import os
import re
from slack_sdk import WebClient
from slack_sdk.rtm_v2 import RTMClient

# Load Slack Bot Token (Replace with your actual bot token)
SLACK_BOT_TOKEN = "your-slack-bot-token"
CHANNEL_ID = "your-channel-id"

# Example list of words found in the Bible (you can expand this with a real dataset)
BIBLICAL_WORDS = set(["god", "jesus", "faith", "pray", "heaven", "love", "sin", "grace", "spirit", "holy"])

# Initialize Slack clients
client = WebClient(token=SLACK_BOT_TOKEN)

def count_biblical_words(text):
    """Count how many words in text appear in the Bible."""
    words = re.findall(r'\b\w+\b', text.lower())  # Extract words and lowercase them
    total_words = len(words)
    biblical_count = sum(1 for word in words if word in BIBLICAL_WORDS)

    ratio = biblical_count / total_words if total_words > 0 else 0
    return biblical_count, total_words, ratio

def send_message(channel, text):
    """Send a message to Slack."""
    client.chat_postMessage(channel=channel, text=text)

def handle_message(event):
    """Process incoming Slack messages."""
    if "text" in event and "none of those words were in the bible" in event["text"].lower():
        original_message = event["text"]  # Assuming this is the message A
        biblical_count, total_words, ratio = count_biblical_words(original_message)
        
        reply_text = f"Actually, {biblical_count} out of {total_words} words ({ratio:.2%}) were in the Bible."
        send_message(CHANNEL_ID, reply_text)

# Connect to Slack using RTM (Real-Time Messaging)
rtm_client = RTMClient(token=SLACK_BOT_TOKEN)

@rtm_client.on("message")
def message_listener(event):
    handle_message(event)

print("Listening for messages...")
rtm_client.start()
