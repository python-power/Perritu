import discord
import re
import youtube_dl
import urllib.parse
import urllib.request
from discord.ext import commands
from ytdl import YTDLSource

client = commands.Bot(command_prefix = '_')
client.remove_command('help')
archivo = open("hello.txt", "r") 
for linea in archivo.readlines():
    TOKEN= linea
archivo.close()

@client.event
async def on_command_error(error, ctx):
	print(error)
	await error.send("pero loco escribe algo xd")

@client.event
async def on_ready():
	print("Perritu esta listo para carrear!")
	await client.change_presence(activity=discord.Game(name='a ser un gato'))
	
@client.command()	
async def help(ctx):
	embed = discord.Embed(
		colour = discord.Colour.dark_purple()
	)

	embed.set_author(name="Como tu ere' bruto aqui te digo como usarme :v")
	embed.add_field(name='_perritu', value='Si estan tan aburrido, puedes hablarme con este comando :dog:', inline=False)
	embed.add_field(name='_play',  value='Pongo esa canción', inline=True)
	embed.add_field(name='_queue', value='Pongo es canción en cola', inline=True)
	embed.add_field(name='_stop', value='Quito la musica', inline=True)
	embed.add_field(name='_pause', value='Pauso la musica', inline=True)
	embed.add_field(name='_resume', value='Quito la pausa', inline=True)
	embed.add_field(name='_di', value='Digo lo que quieras :v', inline=True)

	await ctx.send(embed=embed)

@client.command()
async def play(ctx, *, cancion, channel: discord.VoiceChannel=None):

	try:
		channel = ctx.author.voice.channel
	except:
		await ctx.send("Pero maldito loco a donde tu quiere que yo entre? :rolling_eyes:")
		
	try:
		await ctx.message.add_reaction(emoji="▶")
		vc = await channel.connect()
		async with ctx.typing():
			player = await YTDLSource.from_url(cancion, loop=client.loop, stream=True)
			ctx.voice_client.play(player, after=lambda e: print("error") if e else None)
		await ctx.send('Esta sonando: **{}**'.format(player.title))
	except:
		print("No hay canal de voz al cual unirse")

@client.command()
async def volumen(ctx, volume: int):
	if ctx.voice_client is None:
		return await ctx.send("No estas conectado en un canal de voz :v")
	
	ctx.voice_client.source.volume = volume / 100
	await ctx.send("Volumen cambiado a {}%".format(volume))

@client.command()
async def pause():
	pass

@client.command()
async def stop(ctx):
	await ctx.message.add_reaction(emoji="⏹")
	await ctx.send("Na' hablamos orita :v")
	await ctx.voice_client.disconnect()

@client.command()
async def resume():
	pass			

@client.command()
async def di(ctx,*, msj):
	await ctx.send("**"+msj+"**")
	
client.run(TOKEN)