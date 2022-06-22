import discord
from discord.ext import commands



class locked_channel(commands.Cog, name='locked_channel'):

    def __init__(seft,bot):
        seft.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(seft,ctx, channel : discord.TextChannel=None):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send('Channel locked.')


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(seft,ctx, channel : discord.TextChannel=None):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send('Channel unlocked.')

    @lock.error
    async def lock_error(self,ctx, error):
        if isinstance(error,commands.CheckFailure):
            await ctx.send('You do not have permission to use this command!')

    @unlock.error
    async def lock_error(self,ctx, error):
        if isinstance(error,commands.CheckFailure):
            await ctx.send('You do not have permission to use this command!')




def setup(bot):
    bot.add_cog(locked_channel(bot))
    print("locked channel cog is loaded !")