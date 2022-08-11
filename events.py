import discord
from discord.ext import commands
import json
from datetime import datetime
from discord import Embed
from discord.utils import get

class Events(commands.Cog):

    def __init__(self,bot : commands ):
        self.bot = bot
        self.emoji = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3',
                      '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001F51F']
                    
    @commands.command()
    async def poll(self, ctx, question, *options: str):
        if len(options) > 5:
            await ctx.send("you can only send a maximum of 5 options")
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
    
    @commands.command()
    async def poll2(self, ctx):
        options = "very little","okay","fair","a lot","very"
        if len(options) > 5:
            await ctx.send("you can only send a maximum of 5 options")
        else:
            embed = Embed(title = "poll",description = "How stressful did you feel about this puzzle? ",colour =  ctx.author.colour,timestamp = datetime.utcnow())
            fields = [("Options","\n".join([f'{self.emoji[index]} {option} \n' for index, option in enumerate(options)]),False)]
            #embed.setthumbnail(urllink)
            for name,value, inline in fields:
                embed.add_field(name = name,value = value,inline = inline)
                
            message = await ctx.send(embed = embed)

            for i in range(5):
                await message.add_reaction(self.emoji[i])
    
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
        print(mem)
        """for all members with the role tester, get their id and put them in a list. then for each id in the list, make a private channel with them. """

    async def make_channel(self,ctx):
        guild = ctx.guild
        member = ctx.author
        admin_role = get(guild.roles, name="Admin") #change admin here to guinea pig
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            member: discord.PermissionOverwrite(read_messages=True),
            admin_role: discord.PermissionOverwrite(read_messages=True)}
        channel = await guild.create_text_channel('secret', overwrites=overwrites)

def setup(bot):
    bot.add_cog(Events(bot))
        
