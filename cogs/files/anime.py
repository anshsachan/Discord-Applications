import discord
from discord.ext import commands

class Anime(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def amv(self,ctx):
        await ctx.send('Neptun. is here')
        await ctx.send(file=discord.File('cogs/images/image-or-video/Neptun1.mp4'))
    
    @commands.command()
    async def amv2(self,ctx):
        await ctx.send('Neptun. is here :sunglasses: ')
        await ctx.send(file=discord.File('cogs/images/image-or-video/Neptun2.mp4'))

    @commands.command()
    async def amv3(self,ctx):
        await ctx.send('Neptun. is here :rolling_eyes: ')
        await ctx.send(file=discord.File('cogs/images/image-or-video/Neptun3.mp4'))

    @commands.command()
    async def amv4(self,ctx):
        await ctx.send('Boruto ? ')
        await ctx.send(file=discord.File('cogs/images/image-or-video/Neptun4.mp4'))



def setup(bot):
    bot.add_cog(Anime(bot))
    print("Anime cog is loaded !")