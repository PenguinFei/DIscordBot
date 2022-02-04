import discord
from discord.ext import commands
from core.classes import Cog_Extention
import requests

def true_url(url):
    try:
        request = requests.get(url)
        if requests.status_codes == 200:
            return True
    except:
        return False

class pixiv(Cog_Extention):
    @commands.command()
    async def pix(self, ctx,* ,msg):
        if true_url(f'https://pixiv.cat/{msg[-8:]}.jpg'): 
            await ctx.send(f'https://pixiv.cat/{msg[-8:]}.jpg')
        else:
            x = 1
            while true_url(f'https://pixiv.cat/{msg[-8:]}-{x}.jpg'):
                await ctx.send(f'https://pixiv.cat/{msg[-8:]}-{x}.jpg')
                x += 1

def setup(bot):
    bot.add_cog(pixiv(bot))
