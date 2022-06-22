from operator import sub
import discord
from discord.ext import commands



class Mod(commands.Cog, name='Moderation'):

    def __init__(seft,bot):
        seft.bot = bot



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(seft,ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)

    @clear.error
    async def clear_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please Specify The Number of Messages To Delete !')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(seft,ctx, member: discord.Member , * , reason=None):
        await member.kick(reason=reason)
        await ctx.send(f' {member.name} Was Successfully Kicked For {reason}')


    @kick.error
    async def ban_error(seft,ctx , error):
        if isinstance(error, commands.MissingRequiredArgument):
           await ctx.send('Please Mention a User To Kick')



    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(seft,ctx, member: discord.Member , * , reason=None):
        await member.ban(reason=reason)
        await ctx.send(f' {member.name} Was Successfully Banned For {reason}')

    @ban.error
    async def ban_error(seft,ctx , error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please Mention a User To Banned')



    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx, user: discord.User):
        guild = ctx.guild
        mbed = discord.Embed(
            title = 'Done ! ',
            description = f"{user}Has successfully been unbanned"
        )
        if ctx.author.guild_permissions.ban_members:
            await ctx.send(embed=mbed)
            await guild.unban(user=user)

    @unban.error
    async def unban_error(self,ctx , error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please Specify a User to unban.')


    @commands.command(description="Mutes the specified user.")
    @commands.has_permissions(manage_messages=True)
    async def mute(self,ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(f"Muted {member.mention} for reason {reason}")
        await member.send(f"You were muted in the server {guild.name} for {reason}")

    @commands.command(description="Unmutes a specified user.")
    @commands.has_permissions(manage_messages=True)
    async def unmute(self,ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await ctx.send(f"Unmuted {member.mention}")
        await member.send(f"You were unmuted in the server {ctx.guild.name}")



def setup(bot):
    bot.add_cog(Mod(bot))
    print("Moderation cog is loaded !")