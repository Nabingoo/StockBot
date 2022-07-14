import discord
from discord.ext import tasks, commands
from discord import Embed
import yfinance as yf
import threading
intents = discord.Intents.default()


    

intents.guilds = True

activity = discord.Activity(type=discord.ActivityType.listening, name="test")
bot = commands.Bot(command_prefix = "?", intents = intents, activity=activity, status=discord.Status.online)



@tasks.loop(seconds=60) # task runs every 60 seconds
async def stockupdate():
    await bot.wait_until_ready()
    stock_info = yf.Ticker('TSLA').info
    # stock_info.keys() for other properties you can explore
    market_price = stock_info['regularMarketPrice']
    previous_close_price = stock_info['regularMarketPreviousClose']
    print('market price ', market_price)
    print('previous close price ', previous_close_price)
    math1 = (market_price - previous_close_price)
    math2 = math1 / previous_close_price
    math3 = math2 * 100
    math4 = round(math3, 2)
    await bot.get_guild(942153314915713126).me.edit(nick=str(market_price))
    await bot.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.listening, name= str(math4)+ " | TSLA"))



@bot.command()
async def edit(ctx):
    await ctx.me.edit(nick="101")
    await ctx.channel.send("Test!")


stockupdate.start()

#bot.get_guild(942153314915713126).me.edit(avatar=f))

@bot.command()
async def pfp(ctx):
    with open('tesla.png', 'rb') as image:
        bot.wait_until_ready()
        bot.get_guild(942153314915713126).me.edit(avatar=image.read())


bot.run("OTUwNTgyMzY2NTYzMzY4OTYx.YibA0Q.sBfy0A0LbgsHFGQ6ttiqX8ClKIY")