from colorama import init as colorama_init
from termcolor import colored as clr, cprint as cpr
import ascii.folder
from comm.index import *
from os import system
from random import randint
import sys
colorama_init()

system('cls')

_M, _ssy = 'z', ' --'
_ascii = {'zt': ascii.folder.request('zt')}
_color = ['red', 'green', 'blue', 'yellow', 'white']
_output = {'--mode': clr('zTerminal Mode: %s'%_M, 'white', 'on_blue'), '--help': clr(ascii.folder.request('help'), 'white')}

def script(_fn, v=''):
	v=open(_fn.split(_ssy)[1], 'r', encoding='utf8').read().split('\n')
	print(v)
	for x in range(len(v)):
		if v[x] != '':
			v[x] = v[x][1:]
			print(v[x])
			if v[x].split(_ssy)[0] in _cli:
				_cutin = len(v[x].split(_ssy)[0])
				_attrs = v[x][_cutin:]
			else:
				_attrs = ''
			if _attrs != '':
				_func[v[x].split(_ssy)[0]](_attrs)
			else:
				_func[v[x].split(_ssy)[0]]()
			print(clr('"%s" -> ERROR'%v[x], 'white', 'on_red'))
			try:
				print(_serr[v[x]].split(_ssy)[0])
			except:
				pass
_func = {'die': ex,
		 'ont': ont,
		 'discord.bot.mem': discord_new_memory,
		 'discord.bot.start': discord_run,
		 'discord.bot.event.new': discord_new_event,
		 'discord.bot.event': discord_update_event,
		 'discord.bot.react': discord_reaction_event,
		 'script.src': script,
		 'cts': cts}
_cli = ['discord.bot.start', 'script.src', 'discord.bot.event', 'discord.bot.mem', 'discord.bot.react']
_serr = {'discord.bot.start': clr('0: Check if you set Token attr\n1: Check if your token correct', 'white', 'on_red'),
		 'script.src': clr('0: Remember put " --" before *.zt file', 'white', 'on_red')}

print(clr(_ascii['zt'], 'blue'))

def Mode(Z, x=''):
	if Z == 'z':
		x = input(' Z\ > ')
		if x[0] != '$':
			try:
				print(_output[x])
			except:
				print(clr('"%s" -> ERROR'%x, 'white', 'on_red'))
		else:
			if x[1:].split(_ssy)[0] in _cli:
				_cutin = 1+len(x[1:].split(_ssy)[0])
				_attrs = x[_cutin:]
			else:
				_attrs = ''
			if _attrs != '':
				_func[x[1:].split(_ssy)[0]](_attrs)
			else:
				_func[x[1:].split(_ssy)[0]]()
			print(clr('"%s" -> ERROR'%x, 'white', 'on_red'))
			try:
				print(_serr[x[1:].split(_ssy)[0]])
			except:
				pass
	elif Z == 'cmd':
		x = input(' CMD\ >')
while True:
	Mode(_M)