from os import kill
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt

class gifs(commands.Cog, name='gifs'):

    def __init__(seft,bot):
        seft.bot = bot

    @commands.command()
    async def Dance(self,ctx):
        await ctx.send('Ok')
        await ctx.send('https://tenor.com/view/chika-chika-dance-anime-anime-dance-dance-gif-13973731')

    @commands.command()
    async def kill(self,ctx, user: discord.User):
        await ctx.send('Hmm')
        await ctx.send('https://tenor.com/view/kill-me-baby-gif-5840101')

    @kill.error
    async def kill_error(self,ctx , error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('❌Please Tag a User.❌')

    @commands.command()
    async def slap(self,ctx, user: discord.User):
        await ctx.send('oof!')
        await ctx.send('https://tenor.com/view/slap-gif-19326818')

    @slap.error
    async def slap_error(self,ctx , error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('❌Please Tag a User.❌')

    @commands.command()
    async def cry(self,ctx):
        embed = discord.Embed(
            color =(0x2ECC71)
        )
        embed.set_thumbnail(url = ctx.guild.icon_url)
        embed.set_footer(text=f"{ctx.author} is Crying ... ")


def setup(bot):
    bot.add_cog(gifs(bot))
    print("gifs cog is loaded !")