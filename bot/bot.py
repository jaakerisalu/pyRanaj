import time

import settings

from handler import CommandHandler
from parsing import parse_slack

from slackclient import SlackClient


slack_client = SlackClient(settings.SLACK_API_TOKEN)

if __name__ == "__main__":
    DELAY = 1  # seconds
    if slack_client.rtm_connect():
        print("Are you feeling it, Mr. Krabs?")
        while True:
            command, channel = parse_slack(slack_client.rtm_read())
            if command and channel:
                CommandHandler(slack_client, command, channel).handle()
            time.sleep(DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")



