import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '_')
TOKEN = 'NDYyNDU2MTEwNTk1NDQwNjUw.XPKnfA.Bx4S2NwjMNsbiqCPQH_ukmcTjsI'
	
@client.event
async def on_ready():
	print("Perritu esta listo para carrear!")
	await client.change_presence(activity=discord.Game(name='a ser un gato'))

client.run(TOKEN)