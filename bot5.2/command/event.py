from discord.ext import commands 
import discord
import json
from core.classes import Cog_Extention

with open('settings.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extention):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        #print("Join success")
        channel = self.bot.get_channel(int(jdata['welcome_channel']))
        await channel.send(f'Welcome {member.name} !!!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        #print("Left success")
        channel = self.bot.get_channel(int(jdata['leave_channel']))
        await channel.send(f'Goodbye {member.name} !!!')

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



def setup(bot):
    bot.add_cog(Event(bot))