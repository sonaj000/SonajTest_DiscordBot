from time import sleep
import discord
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
import json
import random
import asyncio

load_dotenv()
Discord_Token = os.getenv("discord_token")
intents = discord.Intents().all() #
intents.members = True
client = discord.Client(intents=intents) #our bot

help_words = ["help", "don't know", "why","not sure", "how"]

bot = commands.Bot(command_prefix= '!',intents=intents)

 #making it seem like the bot is typing 
"""async def typing(ctx):
    #start typing
    async with ctx.typing():
        await asyncio.sleep(2)"""

@bot.command() #reply command
async def foo(ctx,*replyie):
    async with ctx.typing():
        await asyncio.sleep(2)
    try:
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        joined = ' '.join(replyie)
        author = message.author
        await ctx.author.send(joined)
    except:
        await ctx.send("please make sure to you reply to the message with the command")
        print("make sure you reply to the message to send the dm")


@bot.command()
async def ping(ctx):
    print("this is ping")
    await ctx.channel.send("pong")

@bot.event
async def on_ready():
        print('We have logged in as {0.user}'.format(bot))
        #testing
        test_channel = bot.get_channel(999386683281768448)
        test_server = bot.get_guild(972381779904327700)
        await test_channel.send("Hi. This is SonajTest Bot at your service!")

    
@bot.listen()
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        #run the bot chat here 
    
    if message.author == client.user:
        return
    fromtoday = []
    msg = message.content #any message 
    #we can use this to check for any words in the msg like help or whatever. 

    if message.channel.type.name == "private" and any(word in msg for word in help_words):
        dm_channel =bot.get_channel(1003891273918324806) #whichever channel we will end up using for the private one
        dm = await dm_channel.send("I received a DM from " + str(message.author) + " saying " + message.content)
    #this will send the message into the dm channel
    #implement a very fun functionality with discord bot seeming able to type possibly?
    #in order to reply to the user, we simply just need to reply to the message. 
    #check if the message is a reply in the dm channel(two boolean checks)
    #if so, make this a command or start eith 'get' get the author of the message it is referencing and send the dm or reply to them. """


bot.load_extension("Inspire")
bot.load_extension("events")

bot.run('OTk5MTEzNTc1NTg1MDIyMDEy.GsL6LH.LCitOoB6Cyd45jnFGPehubL2CTFI8a9l3YUQxg')
