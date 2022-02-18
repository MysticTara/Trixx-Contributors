#This is file that we need so don't touch 

import discord
from discord.ext import commands, tasks
import random
import os
import keep_alive
from itertools import cycle
import aiohttp
import requests
from requests import get
import json



#This is template for a command so u can use it for anything 
@client.command()
async def commandname(ctx):
  embed=discord.Embed(title="YourTitle", description="YourDescription", color=0xffffff)
  embed.set_image(url="-url-")
  embed.set_thumbnail(url="-url-")
  embed.add_field(name="extrafield", value="extravalue", inline=False)
  embed.set_footer(text="YourFooter")
  
  await ctx.send(embed=embed)    
