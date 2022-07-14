import cloudscraper
import json
import discord
from discord.ext import tasks, commands
from discord import Embed
import yfinance as yf
import threading
intents = discord.Intents.default()


    

intents.guilds = True

activity = discord.Activity(type=discord.ActivityType.watching, name="Working...")
bot = commands.Bot(command_prefix = "?", intents = intents, activity=activity, status=discord.Status.online)

@tasks.loop(seconds=60) # task runs every 60 seconds
async def stockupdate():
    await bot.wait_until_ready()
    await bot.get_guild(942153314915713126).me.edit(nick="F8 Floor Price: " + str(get_floor_prices("the-f8-club-original-nft")[0]))
    await bot.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name= "Floor Price: " + str(get_floor_prices("the-f8-club-original-nft")[0])))



def filter_typename(dict):
  return dict["__typename"] == "AssetQuantityType"

def filter_quantityInEth_exists(dict):
  if "quantityInEth" in dict:
    return True
  else:
    return False

def get_floor_price_in_eth(dict):
  return float(dict["quantity"]) / 1000000000000000000

def get_floor_prices(slug):
  scraper = cloudscraper.create_scraper(
    browser={
      'browser': 'chrome',
      'platform': 'android',
      'desktop': False
    }
  )
  url = "https://opensea.io/collection/{}?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW".format(slug);
  html = scraper.get(url).text
  json_string = html.split("</script>",2)[0].split("window.__wired__=",2)[1]
  data = json.loads(json_string)
  data_values = data["records"].values() # get all values type...
  data_list = [*data_values] # convert to list =~ array in js
  data_list = list(filter(filter_typename, data_list))
  data_list = list(filter(filter_quantityInEth_exists, data_list))
  data_list = list(map(get_floor_price_in_eth, data_list))
  return data_list



# scraping floor prices from opensea

print("RUNNING FOR F8")

print(get_floor_prices("the-f8-club-original-nft"))
firstElement = (get_floor_prices("the-f8-club-original-nft")[0])
print(firstElement)



stockupdate.start()



bot.run("OTUwNTgyMzY2NTYzMzY4OTYx.YibA0Q.sBfy0A0LbgsHFGQ6ttiqX8ClKIY")
