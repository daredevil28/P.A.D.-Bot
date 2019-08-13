import discord
import io
from discord.ext import commands

class OwnerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.group(hidden=True)
    @commands.is_owner()
    async def change(self, ctx):
        if ctx.invoked_subcommand is None:
            pass

    @change.command()
    async def name(self, ctx, *, arg):
    	await ctx.bot.user.edit(username=arg)

    @change.command()
    async def avatar(self, ctx):
    	avtmp = io.BytesIO()
    	await ctx.message.attachments[0].save(avtmp,seek_begin=True)
    	buffer = avtmp.read()
    	await ctx.bot.user.edit(avatar=buffer)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def say(self, ctx, *, arg):
        await ctx.message.delete()
        await ctx.send(arg)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send("shutting down...")
        await ctx.bot.change_presence(status=discord.Status.invisible)
        os._exit(0)

def setup(bot):
    bot.add_cog(OwnerCog(bot))
