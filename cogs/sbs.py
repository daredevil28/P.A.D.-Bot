import discord
from discord.ext import commands

class SbsCog:
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(pass_context=True)
	async def access(ctx):
		if ctx.message.channel.id == "538659673469878273":
			member = ctx.message.author
			await ctx.delete()
			if discord.Role(server=discord.Server(id=server), id="439138951916290059") not in member.roles:
				await bot.add_roles(member, discord.Role(server=discord.Server(id=server), id=439138951916290059))
				await bot.send_message(member, "You have recieved access! The IP for the server is starquest.spacebeaverstudios.com. Click this link to see more info about StarQuest and how to get the resource pack! <https://discordapp.com/channels/160246330701250560/351432162232500225?jump=394914296796151808>")


def setup(bot):
	bot.add_cog(SbsCog(bot))