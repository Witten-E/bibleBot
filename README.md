# What is BibleBot

BibleBot is a bot for CSH Slack that fact checks people when they say "none of those words were in the bible" or similar phrases. The logic and the bot are both written in Python with the bot using [Python Slack SDK](https://tools.slack.dev/python-slack-sdk/). [This](https://tools.slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html) site was most helpful.


The bot is hosted in a Docker container. It is hosted at [bible-bot.cs.house](bible-bot.cs.house). The trigger words can be found at line 8 of [biblePython\checkMessage.py](https://github.com/Witten-E/bibleBot/blob/master/biblePython/checkMessage.py)

This is forked from @Mstrodl's "your-first-slack-bot" and I want to give her a huge thanks for the help.


Because I'm bad at git things, this repo did not exist for a while while I was working on the project because I was working out of an outdated repo with my old name attached to it, so apologies for lack of historical evidence.


TODO: 
1. adding profile photo to the bot and updating the username to Robot Jesus (hate working with slack) 
2. adding more trigger words and parameters so people can display whether they the words in/out of bible to be printed or none.