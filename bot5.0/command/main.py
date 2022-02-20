import discord
from discord.ext import commands
from core.classes import Cog_Extention

class Main(Cog_Extention):
    ##ping值
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def info(self, ctx):
        embed=discord.Embed(title="LaPenGuin", url="https://github.com/PenguinFei/DIscordBot", description="Click here to Github for more info", color=0xb020f3)
        embed.set_author(name="PenguinFei", icon_url="https://i.imgur.com/KAHGCeT.jpg")
        embed.set_thumbnail(url="https://i.imgur.com/tBn6LRP.jpeg")
        await ctx.send(embed=embed)

    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit = num + 1)

def setup(bot):
    bot.add_cog(Main(bot))
    