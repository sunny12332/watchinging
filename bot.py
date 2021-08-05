import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">>i am online<<")

@bot.event
async def on_member_join(member):
   print(f'{member} join!')

@bot.event
async def on_member_remove(member):
   print(f'{member} leave!')
   


bot.run("ODcyNjI1MDYzOTQ4NTkxMTM0.YQslaw.2FIw42a0xPjQgTxzH88DJRFAfOM")




