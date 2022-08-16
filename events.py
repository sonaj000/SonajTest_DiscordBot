from cmath import nan
import string
import discord
from discord.ext import commands
import json
from datetime import datetime
from discord import Embed
from discord.utils import get

client = commands.Bot(command_prefix='!')


class Events(commands.Cog):

    def __init__(self,bot : commands ):
        self.bot = bot
        self.emoji = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3',
                      '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001F51F']
        self.emotions = ["joy","anger","disgust","fear","sadness","surprise"]
        self.playtesters = {}
                    
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
    async def get_channel(self,ctx,name : int):
        guild = ctx.guild
        print(guild)
        channel = discord.utils.get(guild.text_channels, name=str(name))
        print("channel name is: ",channel.name)
        print(self.playtesters)

    @commands.command()
    async def test_role(self,ctx):
        #find all members with this role and get their id and stuff
        want_id = 1007069106811457599 #role id for guinea pig
        mem = []
        for member in ctx.guild.members:
            for role in member.roles:
                if role.id == want_id:
                    mem.append(member.id)
                    break
        for i in mem:
            self.playtesters[i] = nan

        print(len(self.playtesters)) 
        counter = 0
        #if channel already exists ignore
        for key in self.playtesters:
            #if get channel is wrong then bleh 
            await self.make_channel(ctx, counter)
            channel = discord.utils.get(ctx.guild.channels, name= str(counter))
            self.playtesters[key] = channel
            counter += 1
        print(self.playtesters)
    
    @commands.Cog.listener()
    async def on_message(self,message):
        print("triggered")
        msg = message.content #any message 
    #we can use this to check for any words in the msg like help or whatever. 

        if message.channel.type.name == "private":
            dm_channel = self.playtesters[message.author.id] #whichever channel we will end up using for the private one
            dm = await dm_channel.send("I received a DM from " + str(message.author) + " saying " + message.content)
        else:
            print("nope")

    """for all members with the role tester, get their id and put them in a dictionary. make a private channel for each member and get the id of each channel and put themin the dictionary, 
    if the dm is private and message.author.role == any of the playtesters, find the member id in the dictionary and sends its dm to the corresponding channel"""

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome to Dork Dock {0.mention}. I have no clue what I am doing but das okay daijoubu'.format(member))


def setup(bot):
    bot.add_cog(Events(bot))
        
