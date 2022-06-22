import discord
from discord.ext import commands
import asyncio



class timer(commands.Cog, name='timer'):

    def __init__(seft,bot):
        seft.bot = bot


    

    @commands.command()
    async def timer(seft,ctx, seconds):
        try:
            secondint = int(seconds)
            if secondint > 300:
                await ctx.send("I don't think I can go over 5 mins.")
                raise BaseException
            if secondint <= 0:
                await ctx.send("I don't think I can do Negatives")
                raise BaseException

            message = await ctx.send(f"Timer: {seconds}")
        
            while True:
                secondint -= 1
                if secondint == 0:
                    await message.edit(content="Ended !")
                    break
            
                await message.edit(content=f"Timer: {secondint}")
                await asyncio.sleep(1)
            await ctx.send(f"{ctx.author.mention}, Your countdown has been ended !")
        except ValueError:
            await ctx.send('You must enter a number !')



def setup(bot):
    bot.add_cog(timer(bot))
    print("timer cog is loaded !")