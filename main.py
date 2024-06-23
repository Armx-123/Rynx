import random
import discord
from discord.ext import commands
from discord.ui import View , Button
import requests
import aiohttp
import time
import json
import os
bot = commands.Bot(command_prefix="/", intents = discord.Intents.all())


@bot.event
async def on_ready():
    
    await bot.change_presence(status=discord.Status.idle,activity=discord.Game("/auric"))
    print("Bot is Ready")

    try:
        synced = await bot.tree.sync()
        print(f"Synces {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="say",description="This Command creates QR code !")
async def roll(interaction: discord.Interaction,text:str):
    await interaction.channel.send(text)
    ephemeral=True

bot.run(os.environ['TOKEN'])

