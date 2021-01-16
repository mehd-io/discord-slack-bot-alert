# :robot: Discord Slack Alert Bot
Dead simple discord bot that send a Slack message to a given channel when someone enter a Discord Voice channel.

Tech stack : 
* Python 3.9
* Poetry
* Heroku

## Pre-requisite
* Discord
  * Create discord app and bot
  * Retrieve your bot token
  * Invite the bot to your server
  * Retrieve the discord voice channel ID you want the bot to watch
* Slack
  * Add the incoming webhook app
  * Retrieve the webhook that would authorized to send message to a given channel
* Heroku account (for deployement)

## Deployment
Deployment is using [Heroku]('https://www.heroku.com). It provides 550 hours (unverified account) + 450 hours (verified account) of free `dyno` hours per month which is more than enough to run a 24/7 up bot.

Login/Create app
```
heroku login
heroku create -a discord-slack-bot-alert
```

Add poetry build back
```
heroku buildpacks:clear -a discord-slack-bot-alert 
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git -a discord-slack-bot-alert
heroku buildpacks:add heroku/python -a discord-slack-bot-alert
```

Set py runtime + poetry version
```
heroku config:set PYTHON_RUNTIME_VERSION=3.9.1 -a discord-slack-bot-alert
heroku config:set POETRY_VERSION=1.0.0 -a discord-slack-bot-alert
```

Provision environment variables (discord token, etc)

`.env` file should look like this : 
```
SLACK_WEBHOOK=myslackwebhook
CHANNEL_ID=1234
DISCORD_TOKEN=mydiscordbottoken
SERVER_ID=12345
```
`SERVER_ID` is just to have a direct URL to the channel in the slack message

Then deploy the env to your heroku app

```
heroku config:set $(cat .env | sed '/^$/d; /#[[:print:]]*$/d') -a discord-slack-bot-alert
```
Deploy the app
```
git remote add heroku git@heroku.com:discord-slack-bot-alert.git
heroku keys:add
git push heroku main
heroku ps:scale worker=1
```