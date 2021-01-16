import discord
from slack_webhook import Slack
from decouple import config

SLACK_WEBHOOK = config("SLACK_WEBHOOK", cast=str)
CHANNEL_ID = config("CHANNEL_ID", cast=int)
SERVER_ID = config("SERVER_ID", cast=int)
DISCORD_TOKEN = config("DISCORD_TOKEN", cast=str)
DISCORD_HOST = "https://discord.com/channels"

client = discord.Client()
slack = Slack(url=SLACK_WEBHOOK)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == CHANNEL_ID:
            message = f":discord: *{member.name}* entered the <{DISCORD_HOST}/{SERVER_ID}/{CHANNEL_ID}|War Room> to :male-technologist:"
            print(message)
            slack.post(text=message)


client.run(DISCORD_TOKEN)
