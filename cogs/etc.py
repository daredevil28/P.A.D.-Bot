import discord
from discord.ext import commands

class EtcCog:
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def age(self, ctx, member : discord.User = None):
		if member is None:
			member = ctx.message.author
		await ctx.send("{0.name}'s account is created at {0.created_at}".format(member))

	@commands.group()
	async def info(self, ctx):
		if ctx.invoked_subcommand is None:
			pass

	@info.command()
	async def user(self, ctx, arg):
		if ctx.invoked_subcommand is None:
			user = ctx.message.author
		else:
				
			

def setup(bot):
	bot.add_cog(EtcCog(bot))