from discord.ext import commands
from discord import utils
import discord
import asyncio

class modmail(commands.Cog):

    def __init__(seft,bot):
        seft.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if isinstance(message.channel, discord.DMChannel):
            guild = self.bot.get_guild(805449733278531634)
            categ = utils.get(guild.categories, name = "Modmail tickets")
            if not categ:
                overwrites = {
                    guild.default_role : discord.PermissionOverwrite(read_messages = False),
                    guild.me : discord.PermissionOverwrite(read_message = True)
                }
                categ = await guild.create_category(name = "Modmail tickets", overwrites = overwrites)

            channel = utils.get(categ.channels, topic = str(message.author.id))
            if not channel:
                channel = await categ.create_text_channel(name = f"{message.author.name}#{message.author.discriminator}", topics = str(message.author.id))
                await channel.send(f"New Modmail created by {message.author.name} <@&891619975750643763>")

            embed = discord.Embed(describe = message.content, color = 0x696969)
            embed.set_author(name= message.author, icon_url = message.author.avatar_url)
            await channel.send(embed = embed)

        elif isinstance(message.channel, discord.TextChannel):
            if message.content.startswith(self.bot.command_prefix):
                pass
            else:
                topic = message.channel.topic
                if topic:
                    member = message.guild.get_member(int(topic))
                    if member:
                        embed = discord.Embed(describe = message.content, colour = 0x696969)
                        embed.set_author(name = message.author, icon_url= message.author.avatar_url)
                        await member.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def close(self, ctx):
        if ctx.channel.category.name == "Modmail tickets":
            await ctx.send("Deleteing channel")
            await asyncio.sleep(3)
            await ctx.channel.delete()


def setup(bot):
    bot.add_cog(modmail(bot))
    print("Modmail cog is loaded !")