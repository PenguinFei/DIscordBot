import discord 
from discord.ext import commands

##統整定義屬性
class Cog_Extention(commands.Cog):
    ##定義
    def __init__(self, bot):
        self.bot = bot
