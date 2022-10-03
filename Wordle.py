from multiprocessing.connection import answer_challenge
import string
import discord
from discord.ext import commands
import json
from datetime import datetime
from discord import Embed
from discord.utils import get
import asyncio
import emoji

#import json file of the words

class Wordle(commands.Cog):
    #make a wordle message 
    #☐   🟩   🟥
    def __init__(self,bot : commands) -> None:
        self.visual =  [":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:"]
        self.answer = "strik"
        self.bot = bot
        self.record = {}
    
    @commands.command()
    async def WordleStart(self,ctx):
        try:
            Word = Wordle(self.bot)
            Word.Show(ctx)
        except:
            await ctx.send("Error")  
  
    async def Show(self,ctx):
        await ctx.send(self.visual)

    @commands.command()
    async def Check(self,ctx, word : string):
        #parse the string
        #if given word is not equal to five charcaters, throw exception
        if (len(word) != 5):
            await ctx.send("Word must be 5 characters long")
            return
            """         elif(word is not in list):
            await ctx.send("word does not exist or we are unfamiliar with the word. please try again")
            return """
        else:
            for i in word:
                for j in self.answer:
                    if word[i] == answer_challenge[j]:
                        self.visual[i] ==  ":green_large_square:"
            await ctx.send(self.visual)

def setup(bot):
    bot.add_cog(Wordle(bot))           
    

                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    


