import discord
from discord.ext import commands
import asyncio
import sys
import traceback
import os

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix = "!", intents = intents)



@bot.command()
async def ping(ctx):
    await ctx.channel.trigger_typing()
    await asyncio.sleep(0)
    await ctx.send(f'Latency is {round(bot.latency * 1000)}ms')


extensions=[
            'cogs.moderation.info',
            'cogs.moderation.Dm',
            'cogs.moderation.timer',
            'cogs.Music.music',
            'cogs.files.anime',
            'cogs.moderation.channel-lock',
            'cogs.files.animelist',
            'cogs.moderation.mod',
            'cogs.modmail.modmail'
]
if __name__== "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Error loading (extenstion)', file=sys.stderr)
            traceback.print_exc()




@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"
    ))
    
    print("Memo艾Utilities is Ready")



loop = asyncio.get_event_loop()
loop.create_task(bot.start('ODg4ODA0MzI0NzQ1MDQ0MDQ4.G3wohA.hFvBY3KcoqFGqI8Xgu4h0vMTECPbDV2ZPOXmBM'))
loop.run_forever()


bot.run('TOKEN')