import discord
from discord.ext import commands
import random

class Inspire(commands.Cog, name = "Inspire"):

    def __init__(self, bot : commands.bot):
        self.bot = bot #this bot for this class is the bot we are inputting in

    @commands.command() #this is equivalent to @bot.command. difference is we need to add command to bot, but since we are loading in the extension, same thing
    async def inspire(self,ctx):
        starter_encouragements = ["Things will be daijoubu!", "Hang in there. Gambate!", "I'm here for you man. Take yo time to heal"]
        await ctx.send(random.choice(starter_encouragements))

    #@commands.cog.listener() is the cog equivalent of bot.listen() and client.on message

    @commands.Cog.listener()
    async def on_message(self,message):
        trigger_words = ['sad','depressed','angry','upset']
        print(message.author)
        print(commands.bot)
        if discord.Member.bot:
            return
        if message.channel.name == "testinput":
            msg = message.content
            await message.channel.send("hope you feel better")
        else:
            print("wrong channel name")
        
def setup(bot):
    bot.add_cog(Inspire(bot))