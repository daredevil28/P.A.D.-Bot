import discord
from discord.ext import commands

class PingCog:
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def ping(self, ctx):
		await ctx.send("pong!")

def setup(bot):
	bot.add_cog(PingCog(bot))