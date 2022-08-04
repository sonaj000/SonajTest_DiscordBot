
import string
import discord
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
import youtube_dl
import requests
import json
import random
import asyncio

#events test python doc for events
#two parts - one is identifying the unrecognized question part 2 is putting messages from one channel into another channel
intents = discord.Intents().all() #
pp = commands.Bot(command_prefix= '!',intents=intents)
async def getmessages(channel : discord.channel):
    messages = await channel.history(limit = 1).flatten()
    """get messages from one discord channel aka the private channel and then send message in another discord channel"""
    Track = []
    for message in messages:
        Track.append(message)
    return Track
        #tie this function to on message

async def getUserID(message):
    user = message.author
    user_id = user.id
    return user_id

async def dm(ctx, id : string, message):
    user=await pp.get_user_info(id)
    await pp.send_message(user, message)
    # This works ^

def check(m):
    if m.reference is not None:
         return True
    return False

async def reply(ctx): #with command 
    channel = ctx.channel #get channel where command was used
    msg = await channel.fetch_message(ctx.message.reference.message_id) #fetching message which command replied to
    return msg.author

async def Nreply(message):
    dm_channel = pp.get_channel(1003891273918324806)
    msg = await dm_channel.fetch_message(message.reference) #fetching message which command replied to
    return msg.author






