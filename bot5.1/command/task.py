import discord
from discord.ext import commands
from core.classes import Cog_Extention
import json, asyncio, datetime

class Task(Cog_Extention):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0

    @commands.command()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        #mention為tag的意思
        await ctx.send(f'Set Channel: {self.channel.mention}')

    @commands.command()
    async def time_set(self, ctx, time):
        #重製時間計數器
        self.counter = 0
        with open('settings.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('settings.json', 'w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent = 4)
        
        #Ctrl K + Ctrl C == 多數同時註解
        #Ctrl K + Ctrl U == 多數同時取消註解
        # async def spam():
        #     await self.bot.wait_until_ready()
        #     self.channel = self.bot.get_channel(944871168832335892)
        #     while not self.bot.is_closed():
        #         await self.channel.send('spam test is starting!!!')
        #         await asyncio.sleep(5)
        # self.bg_task = self.bot.loop.create_task(spam())

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(944871168832335892)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M')
                with open('settings.json', 'r', encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if now_time == jdata['time'] and self.counter == 0:
                    await ctx.channel.send('Task Working!')
                    #使其只會傳送一次
                    self.counter = 1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass

        self.bg_task = self.bot.loop.create_task(time_task())

    

def setup(bot):
    bot.add_cog(Task(bot))

