import discord 
from discord.ext import commands
from core.classes import Cog_Extention
import random
import json

with open('settings.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)


class React(Cog_Extention):
    ##測試用
    @commands.command()
    async def Test(self, ctx):
        await ctx.send('Testing accurate!!!')

    ##骰骰子
    @commands.command()
    async def dice(self, ctx):
        random_dice = random.choice(jdata['dice'])
        pic = discord.File(random_dice)
        await ctx.send(file = pic)

    ##網路圖片(不須discord.File)
    ##記得點選 "複製圖片位置"
    @commands.command()
    async def Ame(self, ctx):
        await ctx.send(jdata['Ame'])

def setup(bot):
    bot.add_cog(React(bot))
