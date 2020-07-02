# bot.py

import os
import random
from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human from of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool Cool Cool Cool Cool Cool, '
            'no doubt no doubt no doubt no doubt'
        )
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN)



