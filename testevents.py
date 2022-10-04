from cmath import nan
from pickle import FALSE
import string
import discord
from discord.ext import commands
import json
from datetime import datetime
from discord import Embed
from discord.utils import get
import asyncio
from discord import ChannelType


class TestEvents(commands.Cog):

    def __init__(self,bot : commands ):
        self.bot = bot
        self.emoji = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3',
                      '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001F51F']
        self.emotions = ["joy","anger","disgust","fear","sadness","surprise"]
        self.playtesters = {}
        self.bTimer = False
                    
    @commands.command()
    async def poll(self, ctx, question, *options: str):
        if len(options) > 6:
            await ctx.send("you can only send a maximum of 6 options")
        else:
            embed = Embed(title = "poll",description = question,colour =  ctx.author.colour,timestamp = datetime.utcnow())
            fields = [("Options","\n".join([f'{self.emoji[index]} {option} \n' for index, option in enumerate(options)]),False)]
            print(fields)
            #embed.setthumbnail(urllink)
            for name,value, inline in fields:
                embed.add_field(name = name,value = value,inline = inline)
                
            message = await ctx.send(embed = embed)

            for item in self.emoji[:len(options)]:
                await message.add_reaction(item)
    
    @commands.command() #finalize this for me what exactly do u want?
    async def poll2(self, ctx):
        options = "😁","😠","💩","😱","😭","😵"
        options2 = ["😁","😠","💩","😱","😭","😵"]
        if len(options) > 6:
            await ctx.send("you can only send a maximum of 5 options")
        else:
            embed = Embed(title = "poll",description = "How stressful did you feel about this puzzle? ",colour =  ctx.author.colour,timestamp = datetime.utcnow())
            fields = [("Options","\n".join([f'{self.emotions[index]} {option} \n' for index, option in enumerate(options)]),False)]
            #embed.setthumbnail(urllink)
            for name,value, inline in fields:
                embed.add_field(name = name,value = value,inline = inline)
                
            message = await ctx.send(embed = embed)

            for i in range(6):
                await message.add_reaction(options2[i])

    async def make_voice(self,ctx,name : int):
        guild = ctx.guild
        member = ctx.author
        print(member)
        admin_role = get(guild.roles, name="Guinea_Pig") #change admin here to guinea pig
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            member: discord.PermissionOverwrite(read_messages=True),
            admin_role: discord.PermissionOverwrite(read_messages=True),
            guild.me: discord.PermissionOverwrite(read_messages=True)
            }
            
        channel = await guild.create_voice_channel(str(name), overwrites=overwrites)
    
    @commands.command()
    async def make_vchannels(self,ctx):
        ec = []
        for c in ctx.guild.voice_channels:
            if c.type == ChannelType.voice:
                ec.append(c.name)
        await ctx.send(ec)
        #if channel already exists ignore
        for key in self.playtesters:
            #if get channel is wrong then bleh 
            channel_name = self.bot.get_user(key)
            await ctx.send(channel_name.name)
            if channel_name.name not in ec:
                await self.make_voice(ctx, channel_name.name) 
        
    
    async def make_channel(self,ctx,name : int):
        guild = ctx.guild
        member = ctx.author
        print(member)
        admin_role = get(guild.roles, name="Guinea_Pig") #change admin here to guinea pig
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            member: discord.PermissionOverwrite(read_messages=True),
            admin_role: discord.PermissionOverwrite(read_messages=True),
            guild.me: discord.PermissionOverwrite(read_messages=True)
            }
            
        channel = await guild.create_text_channel(str(name), overwrites=overwrites)

    @commands.command()
    async def send(self,ctx,name : str, *puzzle):
        try:
            for member in ctx.guild.members:
                if member.name.lower() == name:
                    joined = ' '.join(puzzle)
                    await member.send(joined)
        except:
            await ctx.send("Please double check the format. !send_puzzle name of user puzzle text like !send_puzzle sonaj000 this is the puzzle")

  
    @commands.command()
    async def get_channel(self,ctx,name : int):
        guild = ctx.guild
        print(guild)
        channel = discord.utils.get(guild.text_channels, name=str(name))
        print("channel name is: ",channel.name)
        print(self.playtesters)

    @commands.command()
    async def make_pchannels(self,ctx):
        #find all members with this role and get their id and stuff
        #1007069106811457599
        want_id = 1007069106811457599 #role id for loyalist
        mem = []
        for member in ctx.guild.members:
            for role in member.roles:
                if role.id == want_id:
                    mem.append(member.id)
                    break
        for i in mem:
            self.playtesters[i] = nan

        print(self.playtesters) 
        counter = 0
        #if channel already exists ignore
        ec = []
        for c in ctx.guild.text_channels:
            if c.type.name == "private":
                ec.append(c.name)
        await ctx.send(ec)
        #
        for key in self.playtesters:
            #if get channel is wrong then bleh 
            channel_name = self.bot.get_user(key)
            if channel_name.name not in ec:
                await self.make_channel(ctx, channel_name.name) 
                channel = discord.utils.get(ctx.guild.channels, name= channel_name.name.lower())
                self.playtesters[key] = channel
                counter += 1
        print(self.playtesters)
    
    @commands.command()
    async def timer(self, ctx, seconds):
        try:
            secondint = int(seconds)
            if secondint > 3600:
                await ctx.send("I dont think im allowed to do go above 3600 seconds which is an hour.")
                raise BaseException
            if secondint <= 0:
                await ctx.send("I dont think im allowed to do negatives")
                raise BaseException
            message = await ctx.send("Timer: {seconds}")
            self.bTimer = True
            while (True):
                secondint -= 1
                if self.bTimer == False:
                    await message.edit(content = f"Timer ended with: {secondint} seconds")
                    break
                if secondint == 0:
                    await message.edit(content="Ended!")
                    break
                await message.edit(content=f"Timer: {secondint}")
                await asyncio.sleep(1)
            await ctx.send(f"{ctx.author.mention} Your countdown Has ended!")
        except ValueError:
            await ctx.send("Must be a number!")
    
    @commands.command()
    async def stop(self,ctx):
        self.bTimer = False
        print("is set false")
  
 
    @commands.Cog.listener()
    async def on_message(self,message):
        print("triggered")
        msg = message.content #any message 
    #we can use this to check for any words in the msg like help or whatever.
        if message.channel.type.name == "private":
            try:
                dm_channel = self.playtesters[message.author.id] #whichever channel we will end up using for the private one 
                dm = await dm_channel.send("I received a DM from " + str(message.author) + ":\n " + message.content)
                if message.attachments:
                    for i in range(len(message.attachments)):
                        await dm_channel.send(content=message.attachments[i].url)
            except:
                message.channel.send("some error in the message")
            """if message.attachments:
                    print("pict5ure")
                    await dm_channel.channel.send("image sent",content=message.attachments[0].url)"""


    """for all members with the role tester, get their id and put them in a dictionary. make a private channel for each member and get the id of each channel and put themin the dictionary, 
    if the dm is private and message.author.role == any of the playtesters, find the member id in the dictionary and sends its dm to the corresponding channel"""
        

async def setup(bot):
    await bot.add_cog(TestEvents(bot))
        
