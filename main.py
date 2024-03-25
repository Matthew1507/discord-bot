import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="#", intents=discord.Intents.all())

@client.command()
async def w(ctx, predicted_world_price):
    try:
        predicted_world_price = int(predicted_world_price)
        buy_price = predicted_world_price * 0.6
        buy_price_max = predicted_world_price * 0.7
        buy_price = round(buy_price, 3)
        buy_price_max = round(buy_price_max, 3)
        profit_percentage = (buy_price / 2) + buy_price
        profit_percentage_max = (buy_price_max / 2) + buy_price_max
        sell_price = round(profit_percentage,3)
        sell_price_max = round(profit_percentage_max,3)
        listing_percentage = (0.333 * sell_price) + sell_price
        listing_percentage_max = (0.333 * sell_price_max) + sell_price_max
        listing_price = round(listing_percentage,2)
        listing_price_max = round(listing_percentage_max,2)
        await ctx.send("Buy Price: " + str(buy_price) + " ~ " + str(buy_price_max))
        await ctx.send("Sell Price: " + str(sell_price) + " ~ " + str(sell_price_max))
        await ctx.send("Listing Price: " + str(listing_price) + " ~ " + str(listing_price_max))
    except ValueError:
        await ctx.send("Please provide a valid number for predicted_world_price.")

client.run(os.getenv("TOKEN"))
