# bot.py
import os
import discord
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='.')
status = cycle(['Status 1','Status 2'])

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client.run(TOKEN)