from discord.ext import commands
import discord
import asyncio
import random

# Token
token = 'your token here'

bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())

# Event
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="bot.py"))
    print("Python Bot is online")

# CMDS

# Test CMD
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# Clear CMD
@bot.command()
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'I have deleted `{amount}` messages')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=amount)

# Kick CMD
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

# Ban CMD
@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)


# Run
bot.run(token)
