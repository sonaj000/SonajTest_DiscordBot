from multiprocessing.connection import answer_challenge
from re import I
import string
import discord
from discord.ext import commands
import json
from datetime import datetime
from discord import Embed
from discord.utils import get
import asyncio

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
            cl = ctx.channel
            Word = Wordle(self.bot)
            self.record[cl] = Word
            await Word.Show(ctx)
        except:
            await ctx.send("Error could not be created")  
  
    async def Show(self,ctx):
        await ctx.send(self.visual)
        
    @commands.command()
    async def wc(self,ctx, *puzzle):
        try:
            joined = ' '.join(puzzle)
            await ctx.send(joined)
        except:
            await ctx.send("Please double check the format. !send_puzzle name of user puzzle text like !send_puzzle sonaj000 this is the puzzle")

    async def replace(self,index):
        self.visual[index] = "🟩"

    @commands.command()
    async def Check(self,ctx, word : str):
        #parse the string
        #if given word is not equal to five charcaters, throw exception
        curr_channel = ctx.channel
        try:
            curr_wordle = self.record[curr_channel]
        except:
            await ctx.send("there is no exisitng wordle for this channel, please start a Wordle for this channel using the !WordleStart")
            return
        lowercased = word.lower()
        if (len(word) != 5):
            await ctx.send("Word must be 5 characters long")
            
            """         elif(word is not in list):
            await ctx.send("word does not exist or we are unfamiliar with the word. please try again")
            return """
        else:
            await ctx.send("Word is 5 characters long")
            print(curr_wordle.answer)
            for i in range(len(lowercased)):
                for j in range(len(self.answer)):
                    if lowercased[i] == self.answer[j]:
                        print(lowercased[i])
                        await curr_wordle.replace(i)
            await ctx.send(curr_wordle.visual)

async def setup(bot):
    await bot.add_cog(Wordle(bot))           
    

                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    


