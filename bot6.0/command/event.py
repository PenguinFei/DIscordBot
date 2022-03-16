import discord
from discord.ext import commands
import json
from core.classes import Cog_Extention
import time


with open('settings.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extention):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        #print("Join success")
        channel = self.bot.get_channel(int(jdata['welcome_channel']))
        await channel.send(f'Welcome {member.mention} !!!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        #print("Left success")
        channel = self.bot.get_channel(int(jdata['leave_channel']))
        await channel.send(f'Goodbye {member.mention} !!!')

    #關鍵字判斷(已完成切割判斷)
    @commands.Cog.listener()
    async def on_message(self, msg):
        #宣告已在settings.jsont建立的辭典
        Keywords = jdata['keyword']
        msg_check = msg.content.split(' ')
        #print(msg_check)
        for check in msg_check:
            if check in Keywords and msg.author != self.bot.user:
                #不能ctx.send
                #以偵測的頻道回傳
                await msg.channel.send('detect keywords :' + " " + check)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send('缺少參數')
            time.sleep(2)
            await ctx.channel.purge(limit = 2)    
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send('查無此指令')
            time.sleep(2)
            await ctx.channel.purge(limit = 2)
            

def setup(bot):
    bot.add_cog(Event(bot))