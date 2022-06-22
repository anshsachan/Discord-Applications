import discord
from discord.ext import commands

class Animelist(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def Ansh_list(self,ctx):
        await ctx.send('Ansh Anime list')
        await ctx.send(file=discord.File('cogs/images/animelist/Ansh_Animelist.txt'))
    


def setup(bot):
    bot.add_cog(Animelist(bot))
    print("Animelist cog is loaded !")