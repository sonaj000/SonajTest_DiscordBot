import discord
from discord.ext import commands
import json
from datetime import datetime
from discord import Embed
from discord.utils import get
import asyncio

bot = commands.Bot(command_prefix= '!')

class Timer(commands.Cog):

    def __init__(self, bot : commands):
        self.start = None
        self.bot = bot
        self.bisCounting = False
        self.counter = 0
        self.record = {}

    async def stop(self,ctx):
        self.bisCounting = False

    @commands.command()
    async def create(self,ctx):
        try:
            time = Timer(bot)
            self.record[self.counter] = time
            await ctx.send(f"Timer created... Timer number is {self.counter}")
            self.counter += 1
        except:
            await ctx.send("please recheck your command")
        
    @bot.command()
    async def start(self,ctx, number : int, seconds : int): 
        try:
            await ctx.send(f"Timer {self.record[number]} is about to start")
            dumy = self.record[number]
            de = await dumy.run(ctx,seconds,number)
            while (de == False):
                if de == True:
                    break
                pass
            self.record.pop(number)  
        except ValueError:
            await ctx.send("in order to start the timer, please use command start followed by the timer number and how long u want it to run")
    
    @bot.command()
    async def kill(self,ctx,number : int):
        holder = self.record[number]
        await holder.stop(ctx)
        try:
            await self.record.pop(number)
        except ValueError:
            ctx.send("already deleted")
    
    @bot.command()
    async def check(self,ctx):
        await ctx.send(self.record)
    
    async def run(self,ctx,seconds : int, number : int) -> bool:
        secondint = int(seconds)
        if secondint > 3600:
            await ctx.send("I dont think im allowed to do go above 3600 seconds which is an hour.")
            raise BaseException
        if secondint <= 0:
            await ctx.send("I dont think im allowed to do negatives")
            raise BaseException
        message = await ctx.send("Timer: {seconds}")
        self.bisCounting = True
        while (True):
            secondint -= 1
            if self.bisCounting == False:
                await message.edit(content = f"Timer ended with: {secondint} seconds")
                break
            if secondint == 0:
                await message.edit(content="Ended!")
                break
            await message.edit(content=f"Timer: {secondint}")
            await asyncio.sleep(1)
        await ctx.send(f"{ctx.author.mention} Your countdown Has ended!")
        return True



def setup(bot):
    bot.add_cog(Timer(bot))
    
