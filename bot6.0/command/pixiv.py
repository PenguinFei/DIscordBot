from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from aiohttp import TooManyRedirects
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
    #客製專屬錯誤回應訊息
    @pix.error
    async def pix_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send('缺少8位數')

def setup(bot):
    bot.add_cog(pixiv(bot))




