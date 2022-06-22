import discord
from discord.ext import commands
import asyncio
import sys
import traceback
import os

intents = discord.Intents.default()
intents.members = True


botA = commands.Bot(command_prefix = "!", intents = intents)


@botA.command()
async def ping(ctx):
    await ctx.channel.trigger_typing()
    await asyncio.sleep(0)
    await ctx.send(f'Latency is {round(botA.latency * 1000)}ms')


#botA

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
            botA.load_extension(extension)
        except Exception as e:
            print(f'Error loading (extenstion)', file=sys.stderr)
            traceback.print_exc()




@botA.event
async def on_ready():
    await botA.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Crazy Gang"
    ))
    
    print("Memo艾Utilities is Ready")



loop = asyncio.get_event_loop()
loop.create_task(botA.start('ODg4ODA0MzI0NzQ1MDQ0MDQ4.YUYBiA.vbNjBd1LSiEqQPH2zeNPfDC1RCI'))
loop.run_forever()


botA.run('TOKEN')