from discord.ext import commands 
import discord
import json
import random
import os

with open('settings.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

#intents必須宣告 不然無法抓取成員資訊!!!!
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents = intents)
    
@bot.event
async def on_ready():
    print("<<<Bot in ready>>>")

@bot.event
async def on_member_join(member):
    print("Join success")
    channel = bot.get_channel(941659703849652224)
    await channel.send(f'Welcome @{member.name} !!!')

@bot.event
async def on_member_remove(member):
    print("Left success")
    channel = bot.get_channel(941659755745779713)
    await channel.send(f'Goodbye {member.name} !!!')

@bot.command()
async def load(ctx, extention):
    bot.load_extension(f'command.{extention}')
    await ctx.send(f"Loaded {extention} done")

@bot.command()
async def unload(ctx, extention):
    bot.unload_extension(f'command.{extention}')
    await ctx.send(f"Un-Loaded {extention} done")

@bot.command()
async def reload(ctx, extention):
    bot.reload_extension(f'command.{extention}')
    await ctx.send(f"Re-Loaded {extention} done")


##顯示分類名稱
for Filename in os.listdir('./command'):
    if Filename.endswith('.py'):
        bot.load_extension(F'command.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['token'])  