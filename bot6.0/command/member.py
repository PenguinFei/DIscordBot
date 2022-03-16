from discord.ext import commands
from core.classes import Cog_Extention

class Member(Cog_Extention):
    @commands.command()
    async def members(self, ctx):
        #print(ctx.guild.members)
        online = []
        offline = []
        for member in ctx.guild.members:
            if str(member.status) == 'online' or str(member.status) == 'idle':
                online.append(member)
            else:
                offline.append(member)
        
        await ctx.send(':white_check_mark: Online Members:')
        for x in online:
            await ctx.send(x)
        await ctx.send(':x: Offline Members:')
        for y in offline:
            await ctx.send(y)

def setup(bot):
    bot.add_cog(Member(bot))