import discord
from discord.ext import commands
import mysql.connector

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["mute"])
    @commands.has_permissions(manage_messages=True)
    async def gulag(self, ctx):
    	gulag_file = discord.File('gulag.png')
    	await ctx.send(file=gulag_file)

    


def setup(bot):
    bot.add_cog(ModerationCog(bot))
