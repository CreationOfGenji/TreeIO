import discord
from discord.ext import commands
import logging
import asyncio
import time
import os

bot = commands.Bot(description="Best Boi", command_prefix="T.")

@bot.command()
async def ping():
    "Shows the bots latency."
    t1 = time.perf_counter()
    msg = await bot.say(":zap: **Calculating Latency...** :zap:")
    t2 = time.perf_counter()
    speed =t2 - t1
    await bot.edit_message(msg, f":ping_pong: Pong! Latency: {round(speed * 1000)}ms")

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name="With Trees / T.help", type=0))

@bot.command()
async def test():
    await bot.say("Testing!")

@bot.command()
async def logout():
    await bot.say("BOT IS LOGGING OUT NOW, STAND BY!")
    await bot.logout()

@bot.command()
async def kick(member:discord.Member):
    await bot.kick(member)

@bot.command()
async def ban(member:discord.Member):
    await bot.ban(member)

@bot.command(pass_context = True)
async def say(ctx, *, say: str):
    await bot.delete_message(ctx.message)
    await bot.say(say)

@bot.command(pass_context = True)
async def kill(ctx, *, member : discord.Member = None):
    if member is None:
        await bot.say(ctx.message.author.mention + ", I Cant Kill Someone If You Dont Tell Me Who To Kill!")
        return 

    if member.id == "424612934640074762":
        await bot.say("Cant Kill me ;)")
    elif member.id == "267281046452699136":
        await bot.say("WHY WOULD I KILL MY MASTER?")
    else:
        await bot.say(ctx.message.author.mention + " HAS MURDERED " + member.mention + " . CALL THE POLICE!")
    
bot.run(os.getenv('TOKEN'))
