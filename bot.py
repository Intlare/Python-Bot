from discord.ext import commands
import discord
import random

# Token
token = 'MTAyNzg1ODA0MjI0ODc2MTM0NA.GMYvY5.sYYVkPLoVsvuHrI8KzMcsv0hLW2yCkR13IHD4E'

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
