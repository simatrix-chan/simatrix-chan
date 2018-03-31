import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    if message.content == "?Simatrix-chan prajituri":
        await client.send_message(message.channel, "Poftim, :cookie:! Hey! Minna!! Cine mai vrea prajituri!?" file: "http://pa1.narvii.com/5780/cbffeeffa3935078dcffda0ea853f90260251be1_128.gif") #responds with Cookie emoji when someone says "cookie"

 

client.run("NDI5NzI5MTQ4ODY5NTQxODk4.DaGBPA.CzkMfpnY0n7wNPA9sE4VBo1xOQI") #Replace token with your bots token
