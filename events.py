from sqlite3 import Timestamp
import discord
from discord.ext import commands
import json
from datetime import datetime
from discord import Embed

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
            #embed.setthumbnail(urllink)
            for name,value, inline in fields:
                embed.add_field(name = name,value = value,inline = inline)
                
            message = await ctx.send(embed = embed)

            for item in self.emoji[:len(options)]:
                await message.add_reaction(item)

def setup(bot):
    bot.add_cog(Events(bot))
        
