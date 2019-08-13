import discord
import datetime
from discord.ext import commands



class EtcCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.group()
	async def info(self, ctx):
		if ctx.invoked_subcommand is None:
			pass

@age.error
async def age_error():
	await ctx.send("Useage: p!info [user/age/joined] (username)")

	@info.command()
	async def age(self, ctx, member : discord.User = None):
		if member is None:
			member = ctx.message.author
		await ctx.send("{0.name}'s account is created at {0.created_at}".format(member))

	@info.command()
	async def joined(self, ctx, member : discord.User = None):
		if member is None:
			member = ctx.message.author
		await ctx.send("{0.name} joined at {0.joined_at}".format(member))

	@info.command()
	async def user(self, ctx, member : discord.User = None):
		if member is None:
			user = ctx.message.author.id
		else:
			user = member.id

		memberinfo = await ctx.message.guild.fetch_member(user)
		userinfo = await self.bot.fetch_user(user)

		embed = discord.Embed(color=memberinfo.color, timestamp=datetime.datetime.now())
		embed.set_image(url=userinfo.avatar_url)
		embed.set_footer(text=ctx.message.author.name)
		embed.set_thumbnail(url="https://i.imgur.com/7cgFXCX.png")
			
		roleslist = []

		for x in memberinfo.roles:
			roleslist.append(x.name)
		rolescleaned = ', '.join(roleslist)
		
		embed.set_author(name=userinfo.name, icon_url=userinfo.avatar_url_as(format="png"))
		embed.add_field(name='ID', value=userinfo.id,)
		embed.add_field(name="Nickname", value=memberinfo.display_name)
		embed.add_field(name='Created at D/M/Y', value=userinfo.created_at.strftime('%d-%m-%Y at %X'), inline=True)
		embed.add_field(name="Name", value=userinfo.display_name)

		embed.add_field(name="Joined server D/M/Y", value=memberinfo.joined_at.strftime('%d-%m-%Y at %X'))
		embed.add_field(name="Roles", value=rolescleaned)
		

		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(EtcCog(bot))