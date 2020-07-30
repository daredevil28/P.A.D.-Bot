#import modules
import json
import logging
import sys
import traceback
import discord
from discord.ext import commands

#set logging level
logging.basicConfig(level=logging.INFO)

data = json.load(open("token.json"))
token = data["token"]
owner = data["owner"]

bot = commands.Bot(command_prefix='p!')

sbsChannel = None
sbsServerId = None
role = None

initial_extensions = ['cogs.ping', 'cogs.owner', 'cogs.moderation', 'cogs.music', 'cogs.sbs', 'cogs.etc']

#Load all cogs in the initial_extensions array
if __name__ == '__main__':
	for extension in initial_extensions:
		try:
			bot.load_extension(extension)
			print(f'Loaded extension {extension}.')
		except Exception as e:
			print(f'Failed to load extensions {extension}.', file=sys.stderr)
			traceback.print_exc()


#print when ready
@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))
	global sbsChannel
	global sbsServerId
	global role
	sbsChannel = bot.get_channel(160248030161797121)
	sbsServerId = bot.get_guild(160246330701250560)
	role = sbsServerId.get_role(735321933138362409)


@bot.event
async def on_message(message):
	if message.content.startswith('j!'):
		await message.channel.send('The prefix `j!` is no longer used, the bot now uses the prefix `p!`.\n example: `p!ping`')
	await bot.process_commands(message)


@bot.event
async def on_member_update(before, after):
	if after.guild == sbsServerId:
		if role not in before.roles:
			if role in after.roles:
				await sbsChannel.send("{0.mention} has become a StarquestMinecraft patreon! Thank you very much!\n <https://www.patreon.com/StarQuestMinecraft>".format(after))

bot.run(token, bot=True, reconnect=True)