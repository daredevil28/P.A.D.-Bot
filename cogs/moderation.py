import discord
from discord.ext import commands
import mysql.connector

gulag_file = discord.File('gulag.png')

class ModerationCog:
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def gulag(self, ctx):
    	await ctx.send(file=gulag_file)

    


def setup(bot):
    bot.add_cog(ModerationCog(bot))
