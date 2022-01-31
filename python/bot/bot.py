from discord.ext import commands 
import discord
import json
import random
import os

with open('settings.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix="$")
    
@bot.event
async def on_ready():
    print("<<<Bot in ready>>>")

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



for Filename in os.listdir('./command'):
    if Filename.endswith('.py'):
        bot.load_extension(F'command.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['token'])  