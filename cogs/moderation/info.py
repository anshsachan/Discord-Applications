import discord
from discord.ext import commands
import asyncio
from time import sleep



class info(commands.Cog, name='info'):

    def __init__(seft,bot):
        seft.bot = bot


    @commands.command(help = "Prints details of Server")
    async def info(self,ctx):
        owner=str(ctx.guild.owner)
        region = str(ctx.guild.region)
        guild_id = str(ctx.guild.id)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon_url)
        desc=ctx.guild.description
    
        embed = discord.Embed(
        title=ctx.guild.name + " Server Information",
        description=desc,
        color=discord.Color.blue()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=guild_id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        await self,ctx.channel.trigger_typing()
        await asyncio.sleep(0)
        await ctx.send(embed=embed)

        members=[]
        async for member in self,ctx.guild.fetch_members(limit=150) :
            await self,ctx.channel.trigger_typing()
            await asyncio.sleep(0)
            await ctx.send('Name : {}\t Status : {}\n Joined at {}'.format(member.display_name,str(member.status),str(member.joined_at)))    


def setup(bot):
    bot.add_cog(info(bot))
    print("info cog is loaded !")