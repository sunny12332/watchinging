import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">>i am online<<")

@bot.event
async def on_member_join(member):
   print(f'{member} join!')
   


bot.run("ODcyNjI1MDYzOTQ4NTkxMTM0.YQslaw.0j8r3hfYAr-rWZ0PjLXbky7D-64")




