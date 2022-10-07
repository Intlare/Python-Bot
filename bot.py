from discord.ext import commands
import discord
import random

# Token
token = 'your token here'

bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())

# Event
@bot.event
async def on_ready():
    print("Python Bot is online")

# Commands
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# Run
bot.run(token)
