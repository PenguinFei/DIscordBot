import discord
from discord.ext import commands
from core.classes import Cog_Extention
import json

with open('settings.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)


class roles(Cog_Extention):
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        if data.message_id == int(jdata['role_line']):
            if str(data.emoji) == '🎉':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(944877463014617118)
                await data.member.add_roles(role)
                await data.member.send(f'你在 {guild} 獲得了 {role} 身分組')
    @commands.Cog.listener()        
    async def on_raw_reaction_remove(self, data):
        if data.message_id == int(jdata['role_line']):
            if str(data.emoji) == '🎉':
                guild = self.bot.get_guild(data.guild_id)
                user = guild.get_member(data.user_id)
                role = guild.get_role(944877463014617118)
                await user.remove_roles(role)
                await user.send(f'你在 {guild} 移除了 {role} 身分組')
        
def setup(bot):
    bot.add_cog(roles(bot))