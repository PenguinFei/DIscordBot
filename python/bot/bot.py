from discord.ext import commands 
import discord
import json
import random

with open('settings.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix="$")
    
@bot.event
async def on_ready():
    print("<<<Bot in ready>>>")

##以下為指令區
##ping值
@bot.command()
async def ping(ctx):
    await ctx.send(bot.latency)

##測試用
@bot.command()
async def Test(ctx):
    await ctx.send('Testing accurate!!!')

##骰骰子
@bot.command()
async def dice(ctx):
    random_dice = random.choice(jdata['dice'])
    pic = discord.File(random_dice)
    await ctx.send(file = pic)

##網路圖片(不須discord.File)
##記得點選 "複製圖片位置"
@bot.command()
async def Ame(ctx):
    await ctx.send(jdata['Ame'])


bot.run(jdata['token']) 