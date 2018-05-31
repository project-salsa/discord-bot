import discord
import logging
import sys

from discord.ext import commands

# Initialize the Bot
bot = commands.Bot(command_prefix='?', description='Mecha Rember')
client = discord.Client()

# Initialize the Logger
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Expecting path to token
with open(sys.argv[1], 'r') as f:
    token = f.read()

# On Ready
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

# General Message Processing
@bot.event
async def on_message(message):
    # General Messsage processing happens here
    pass

    # This is needed for the bot to process actual commands
    await bot.process_commands(message)

# Example command
# called in the server via `?example`
@bot.command(pass_context=True)
async def example(ctx):
    await ctx.send("I am an example!")

# run the bot
bot.run(token)