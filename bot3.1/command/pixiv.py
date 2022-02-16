import discord
from discord.ext import commands
from core.classes import Cog_Extention
import requests

class pixiv(Cog_Extention):
    @commands.command()
    async def pix(self, ctx,* ,url):
        r = requests.get(url)
        if(r.status_code == requests.codes.ok):
            await ctx.send('https://pixiv.cat/'+ url[-8:] + '.jpg')
        
def setup(bot):
    bot.add_cog(pixiv(bot))
