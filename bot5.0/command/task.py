import discord
from discord.ext import commands
from core.classes import Cog_Extention
import json, asyncio, datetime

class task(Cog_Extention):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(937573420361719808)
            while not self.bot.is_closed():
                await self.channel.send('The bot is online now!!!')
                await asyncio.sleep(5)
        self.bg_task = self.bot.loop.create_task(interval())

    @commands.command()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        #mention為tag的意思
        await ctx.send(f'Set Channel: {self.channel.mention}')

def setup(bot):
    bot.add_cog(task(bot))

