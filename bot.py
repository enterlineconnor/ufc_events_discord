# Imports
import discord
import event
import creds
from discord.ext import commands

# Credentials
TOKEN = creds.bot['TOKEN']

# Create bot
client = commands.Bot(command_prefix='!')

# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


@client.event
async def on_message(message):
    if message.content.startswith('!event'):
        next_event = event.next_event()
        await message.channel.send(next_event)
    
    if message.content.startswith('!upcoming'):
        upcoming_events = event.upcoming_events()
        await message.channel.send(upcoming_events)

# Command
@client.command()
async def helloworld(ctx):
    await ctx.send('Hello World!')


client.run(TOKEN)