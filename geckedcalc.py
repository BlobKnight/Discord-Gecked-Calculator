import os

import requests
from discord.ext import commands
from dhooks import Embed
import discord
import random
import reddit
from discord import app_commands
from PIL import Image, ImageFont
from PIL import ImageDraw
from youtube_dl import YoutubeDL
import asyncio
import gopy as go
from bs4 import BeautifulSoup
import math
from numpy import loadtxt
import time
import os
from discord.ui import Button, View
from discord.ext.commands import Bot


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)

token = "token"



# class client(discord.Client):
#     async def startup(self):
#         print("Bot is ready!")
#         await self.wait_until_ready()
#         await tree.sync(guild = discord.Object(id = 972712554499559475))

# aclient = client()
# tree = app_commands.CommandTree(aclient)
# @tree.command(guild = discord.Object(id = 972712554499559475), name = "ping", description="Pings the bot")
# async def slash(interaction: discord.interaction):
#     await interaction.response.send_message("Pong!",empheral=True)
@client.event
async def on_ready():
    channel = client.get_channel(898780042732118019)
    await channel.send("I'm online!")

    print("Bot is ready!")


@client.command()
async def calc(ctx, rtReservetime):
    quarter = None
    region = None
    model = None
    time = int(rtReservetime.strip())
    member = ctx.author

    print(member.name)
    modelsMoo = loadtxt('modelsMoo.txt', dtype="int")
    regionsMoo = loadtxt('regionsMoo.txt', dtype="str")
    timesMoo = loadtxt('timesMoo.txt', dtype="int")
    quartersMoo = loadtxt('quartersMoo.txt', dtype="str")

    models = list(modelsMoo)
    regions = list(regionsMoo)
    times = list(timesMoo)
    quarters = list(quartersMoo)
    allDataPoints = len(timesMoo)

    def calculateDate(model, region, quarter):
        filtration(models, model)
        filtration(quarters, quarter)
        if region != "ALL":
            filtration(regions, region)

        if quarter == "Q1":
            daysInQuarter = 34
        elif quarter == "Q2":
            daysInQuarter = 91
        else:
            daysInQuarter = 92

        for x in range(0, len(times)):
            if time >= times[x]:
                userQueuePos = (x + 2)

        ans = daysInQuarter / (len(times) + 1)
        userDate = ans * userQueuePos
        userDate = math.ceil(userDate)

        if userDate < 1:
            userDate = 1

        if quarter == "Q1":
            userDate = (userDate + 3)
        if quarter == "Q2":
            userDate = (userDate + 4)
        if quarter == "Q3":
            userDate = (userDate - 4)
        if quarter == "Q1":
            if userDate > 31:
                userDate = 31
        if quarter == "Q2":
            if userDate > 88:
                userDate = 88
        if quarter == "Q3":
            if userDate > 88:
                userDate = 88

        return userDate

    def removeValue(x):
        models.pop(x)
        quarters.pop(x)
        regions.pop(x)
        times.pop(x)

    def filtration(filterList, filterCondition):
        x = 0
        while x < len(filterList):
            if filterList[x] != filterCondition:
                removeValue(x)
            else:
                x += 1

    button1 = Button(label="Q1", style=discord.ButtonStyle.green)
    button2 = Button(label="Q2", style=discord.ButtonStyle.green)
    button3 = Button(label="Q3 (Beta)", style=discord.ButtonStyle.green)
    button4 = Button(label="All", style=discord.ButtonStyle.green)

    async def q1(interaction):
        global quarter
        quarter = "Q1"
        button1.label = "US"
        button2.label = "EU"
        button3.label = "UK"
        view.add_item(button4)
        button1.callback = US
        button2.callback = EU
        button3.callback = UK
        button4.callback = ALL
        await interaction.response.send_message(ctx.author.mention + " - Select region:", view=view)

    async def q2(interaction):
        global quarter
        quarter = "Q2"
        button1.label = "US"
        button2.label = "EU"
        button3.label = "UK"
        view.add_item(button4)
        button1.callback = US
        button2.callback = EU
        button3.callback = UK
        button4.callback = ALL
        await interaction.response.send_message(ctx.author.mention + " - Select region:", view=view)

    async def q3(interaction):
        global quarter
        quarter = "Q3"
        button1.label = "US"
        button2.label = "EU"
        button3.label = "UK"
        view.add_item(button4)
        button1.callback = US
        button2.callback = EU
        button3.callback = UK
        button4.callback = ALL
        await interaction.response.send_message(ctx.author.mention + " - Select region:", view=view)

    async def US(interaction):
        global region

        region = "US"
        button1.label = "64GB"
        button2.label = "256GB"
        button3.label = "512GB"
        button1.callback = model1
        button2.callback = model2
        button3.callback = model3
        view.remove_item(button4)
        await interaction.response.send_message(ctx.author.mention + " - Select model:", view=view)

    async def EU(interaction):
        global region
        region = "EU"
        button1.label = "64GB"
        button2.label = "256GB"
        button3.label = "512GB"
        button1.callback = model1
        button2.callback = model2
        button3.callback = model3
        view.remove_item(button4)
        await interaction.response.send_message(ctx.author.mention + " - Select model:", view=view)

    async def UK(interaction):
        global region
        region = "UK"
        button1.label = "64GB"
        button2.label = "256GB"
        button3.label = "512GB"
        button1.callback = model1
        button2.callback = model2
        button3.callback = model3
        view.remove_item(button4)
        await interaction.response.send_message(ctx.author.mention + " - Select model:", view=view)

    async def ALL(interaction):
        global region
        region = "ALL"
        button1.label = "64GB"
        button2.label = "256GB"
        button3.label = "512GB"
        button1.callback = model1
        button2.callback = model2
        button3.callback = model3
        view.remove_item(button4)
        await interaction.response.send_message(ctx.author.mention + " - Select model:", view=view)

    async def model1(interaction):
        global model
        global region
        global quarter
        global time
        model = int(64)
        print(model, region, quarter)
        userDate = calculateDate(model, region, quarter)
        exactDate = None
        if quarter == "Q1":
            if userDate <= 3:
                exactDate = ("February", str(userDate + 25))
            else:
                exactDate = ("March", str(userDate - 3))
        elif quarter == "Q2":
            if userDate <= 30:
                exactDate = ("April", str(userDate))
            elif userDate <= 61:
                exactDate = ("May", str(userDate - 30))
            else:
                exactDate = ("June", str(userDate - 61))
        else:
            if userDate <= 31:
                exactDate = ("July", str(userDate))
            elif userDate <= 62:
                exactDate = ("August", str(userDate - 31))
            else:
                exactDate = ("September", str(userDate - 62))
        # embed = discord.Embed(title=userDate)
        embed = discord.Embed(title="Your expected Deck order date is " + " ".join(exactDate),
                              description="Your expected Deck order date is " + " ".join(exactDate))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.set_footer(text="Powered by Gecked Calculator")
        embed.set_thumbnail(url="https://cdn.cloudflare.steamstatic.com/steamdeck/images/press/logos/steam-deck-logos.gif")
        embed.add_field(name="Model", value=str(model)+" GB", inline=False)
        embed.add_field(name="Region", value=region, inline=False)
        embed.add_field(name="Quarter", value=quarter, inline=False)
        embed.add_field(name="Time", value=time, inline=False)
        print(exactDate)
        await interaction.response.send_message(embed=embed)

    async def model2(interaction):
        global model
        global region
        global quarter
        global time
        model = int(256)
        print(model, region, quarter)
        userDate = calculateDate(model, region, quarter)
        exactDate = None
        if quarter == "Q1":
            if userDate <= 3:
                exactDate = ("February", str(userDate + 25))
            else:
                exactDate = ("March", str(userDate - 3))
        elif quarter == "Q2":
            if userDate <= 30:
                exactDate = ("April", str(userDate))
            elif userDate <= 61:
                exactDate = ("May", str(userDate - 30))
            else:
                exactDate = ("June", str(userDate - 61))
        else:
            if userDate <= 31:
                exactDate = ("July", str(userDate))
            elif userDate <= 62:
                exactDate = ("August", str(userDate - 31))
            else:
                exactDate = ("September", str(userDate - 62))
        # embed = discord.Embed(title=userDate)
        print(exactDate)
        embed = discord.Embed(title="Your expected Deck order date is " + " ".join(exactDate))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.set_footer(text="Powered by Gecked Calculator")
        embed.set_thumbnail(
            url="https://cdn.cloudflare.steamstatic.com/steamdeck/images/press/logos/steam-deck-logos.gif")
        embed.add_field(name="Model", value=str(model)+" GB", inline=False)
        embed.add_field(name="Region", value=region, inline=False)
        embed.add_field(name="Quarter", value=quarter, inline=False)
        embed.add_field(name="rtReservetime", value=rtReservetime, inline=False)
        print(exactDate)
        await interaction.response.send_message(embed=embed)
        # await interaction.response.send_message(
        #     ctx.author.mention + " - Your expected Deck order date is " + " ".join(exactDate))

    async def model3(interaction):
        global model
        global region
        global quarter
        global time
        model = int(512)
        print(model, region, quarter)
        userDate = calculateDate(model, region, quarter)
        exactDate = None
        if quarter == "Q1":
            if userDate <= 3:
                exactDate = ("February", str(userDate + 25))
            else:
                exactDate = ("March", str(userDate - 3))
        elif quarter == "Q2":
            if userDate <= 30:
                exactDate = ("April", str(userDate))
            elif userDate <= 61:
                exactDate = ("May", str(userDate - 30))
            else:
                exactDate = ("June", str(userDate - 61))
        else:
            if userDate <= 31:
                exactDate = ("July", str(userDate))
            elif userDate <= 62:
                exactDate = ("August", str(userDate - 31))
            else:
                exactDate = ("September", str(userDate - 62))
        embed = discord.Embed(title="Your expected Deck order date is " + " ".join(exactDate), description="Your expected Deck order date is " + " ".join(exactDate))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.set_footer(text="Powered by Gecked Calculator")
        embed.set_thumbnail(url="https://cdn.cloudflare.steamstatic.com/steamdeck/images/press/logos/steam-deck-logos.gif")
        embed.add_field(name="Model", value=str(model)+" GB", inline=False)
        embed.add_field(name="Region", value=region, inline=False)
        embed.add_field(name="Quarter", value=quarter, inline=False)
        embed.add_field(name="rtReservetime", value=rtReservetime, inline=False)
        print(exactDate)
        await interaction.response.send_message(embed=embed)
        #await interaction.response.send_message(
         #   ctx.author.mention + " - Your expected Deck order date is " + " ".join(exactDate))

    button1.callback = q1
    button2.callback = q2
    button3.callback = q3

    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    await ctx.send(ctx.author.mention + " - select quarter:", view=view)


client.run(token)