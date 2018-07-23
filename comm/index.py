from os import system
from colorama import init as colorama_init
from termcolor import colored as clr, cprint as cpr
import discord, asyncio
colorama_init()

_discord = {'file': 'import discord, asyncio\nclient = discord.Client()\n'}
_ssy = ' --'

def ex():
	exit()

def cts():
	system('cls')

def ont():
	system('start zterminal.py')

def discord_new_event():
	_discord['file'] += "\n@client.event\nasync def on_message(message):"

def discord_update_event(info):
	info = [x for x in info.split(_ssy) if x]
	_discord['file'] += "\n	if message.content.startswith('"+ info[0] +"'):\n		await client.send_message(message.channel, '"+ info[1] + "')"

def discord_reaction_event(info):
	info = [x for x in info.split(_ssy) if x]
	_discord['file'] += "\n	await client.add_reaction(message, '"+ info[0] +"')"

def discord_new_memory(info):
	info = [x for x in info.split(_ssy) if x]
	_discord['file'] += info[0] + '=' + info[1] + '\ndef add' + info[0] + '(int):\n	'+info[0]+' += int\n'

def discord_run(_token, v=''):
	_token = [x for x in _token.split(_ssy) if x]
	print(clr('Token "%s********************" Started'%_token[0][:39], 'white', 'on_blue'))
	_discord['file'] += "\nclient.run('"+ _token[0] +"')"
	v=open('comm/DIS.py', 'w')
	v.write(_discord['file'])
	v.close()
	system('start comm/dis.py')