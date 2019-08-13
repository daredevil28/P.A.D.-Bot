import discord
from discord.ext import commands

class SbsCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	
	@commands.command(pass_context=True, hidden=True)
	async def access(self, ctx):
		#variables
		roleid = 439138951916290059
		channelid = 439139494684262400
		#Did the user send the command in the right channel?
		if ctx.message.channel.id == channelid:

			member = ctx.message.author

			await ctx.message.delete()

			role = ctx.guild.get_role(roleid)
			#Does the user already have the role?
			if role not in member.roles:

				await member.add_roles(role, reason="Join role added")
				await member.send("You have recieved access! The IP for the server is starquest.spacebeaverstudios.com. Click this link to see more info about StarQuest and how to get the resource pack! <https://discordapp.com/channels/160246330701250560/351432162232500225?jump=394914296796151808>")

	@commands.command(pass_context=True, hidden=True)
	async def science(self, ctx):

		roleid = 439700931932585987
		serverid = 160246330701250560

		if ctx.message.guild.id == serverid:
			member = ctx.message.author
			role = ctx.guild.get_role(roleid)

			if role not in member.roles:
				await member.add_roles(role, reason="Requested role")
				await member.send("You have recieved the Scientist role", delete_after=5)
				await asyncio.sleep(5)
				await ctx.message.delete()
				
			else:
				await member.remove_roles(role, reason="Requested removing of role")
				await member.send("You no longer have the Scientist role", delete_after=5)
				await asyncio.sleep(5)
				await ctx.message.delete()

def setup(bot):
	bot.add_cog(SbsCog(bot))