from telnetlib import DM
import discord
from discord.ext import commands

class DM(commands.Cog):

    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def DM(self,ctx,user: discord.Member,*,args):
        if args != None:
            try:
                await user.send(args)
                await ctx.send(f'DM sent to {user.name}')
            except:
                await ctx.send('User has His DMs closed !')
   
    @DM.error
    async def Dm_error(seft,ctx , error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please Mention a User To DM !')


def setup(bot):
    bot.add_cog(DM(bot))
    print("DM cog is loaded !")
