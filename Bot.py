import discord
from discord.ext import commands
import datetime
import os
import sys
d = datetime.datetime.today()

bot = commands.Bot(command_prefix='%',description='testbot')

@bot.event
async def on_ready():
 await bot.say("started")
 print('Logged in as')
 print(bot.user.name)


@bot.command()
async def hello():
 await bot.say("hello")
 print('発言されました')
 print(d)

@bot.command()
async def time():
 await bot.say (d)

@bot.command()
async def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

bot.run('MzY0MDM1NTI0NDU1MDM4OTc3.DLKEXw.V3-6f50x4Ra1Gs5x5hBP23rCNXE')
