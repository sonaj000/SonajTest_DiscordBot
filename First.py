import discord
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
import youtube_dl
import requests
import json
import random
import eventstest

load_dotenv()
Discord_Token = os.getenv("discord_token")
intents = discord.Intents().all() #
client = discord.Client(intents=intents) #our bot

help_words = ["help", "don't know", "why","not sure", "how"]

bot = commands.Bot(command_prefix= '!',intents=intents)

@bot.command()
async def foo(ctx,*replyie):
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
    """if eventstest.check(message) and message.channel.id == 1003891273918324806: 
        print("this is true")
        holder = message
        replie = await eventstest.Nreply(message) #need to fix this this is where it is getting the message it is being replied to
        print(replie)"""

    """
    if message.content.startswith('get'):
        test_channel = client.get_channel(1002138142532440164)
        fromtoday = await eventstest.getmessages(test_channel)
 
        test_channel2 = client.get_channel(999386683281768448)
        for i in fromtoday:
            await test_channel2.send(i.content)
            await i.author.send(i.content) #send indivudal dm
            #await i.reply("replied") #how to reply to the dm 
        #we need to check if the channel is a dm channel for the onmesssage event. """




    


#client.run('OTk5MTEzNTc1NTg1MDIyMDEy.GsL6LH.LCitOoB6Cyd45jnFGPehubL2CTFI8a9l3YUQxg')
bot.run('OTk5MTEzNTc1NTg1MDIyMDEy.GsL6LH.LCitOoB6Cyd45jnFGPehubL2CTFI8a9l3YUQxg')
