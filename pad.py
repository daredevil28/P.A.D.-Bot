#import modules
import discord
import logging
import sys, traceback
import json
from discord.ext import commands

#set logging level
#logging.basicConfig(level=logging.INFO)

data = json.load(open("token.json"))
token = data["token"]
owner = data["owner"]	

bot = commands.Bot(command_prefix='p!')

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

@bot.event
async def on_message(message):
	if message.content.startswith('j!'):
		await message.channel.send('The prefix `j!` is no longer used, the bot now uses the prefix `p!`.\n example: `p!ping`')
	await bot.process_commands(message)

bot.run(token, bot=True, reconnect=True)