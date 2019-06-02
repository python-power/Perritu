import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '_')
client.remove_command('help')
archivo = open("C:/hello.txt", "r") 
for linea in archivo.readlines():
    TOKEN= linea
archivo.close()

	
@client.event
async def on_ready():
	print("Perritu esta listo para carrear!")
	await client.change_presence(activity=discord.Game(name='a ser un gato'))
	
@client.command()	
async def help(ctx):
	embed = discord.Embed(
		colour = discord.Colour.dark_purple()
	)

	embed.set_author(name='Como tu ere bruto aqui te digo como usarme :v')
	embed.add_field(name='_perritu', value='Si estan tan aburrido, puedes hablarme con este comando :dog:', inline=False)
	embed.add_field(name='_play',  value='Pongo esa canción', inline=True)
	embed.add_field(name='_queue', value='Pongo es canción en cola', inline=True)
	embed.add_field(name='_stop', value='Quito la musica', inline=True)
	embed.add_field(name='_vete', value='Me voy de la llamada', inline=True)
	embed.add_field(name='_pause', value='Pauso la musica', inline=True)
	embed.add_field(name='_resume', value='Quito la pausa', inline=True)
	embed.add_field(name='_di', value='Digo lo que quieras :v', inline=True)

	await ctx.send(embed=embed)
	
@client.command()
async def play(ctx, *, channel: discord.VoiceChannel=None):
	if not channel:
		try:
			channel = ctx.author.voice.channel
		except AttributeError:
			raise InvalidVoiceChannel('No channel to join. Please either specify a valid channel or join one.')
	
	vc = ctx.voice_client
	
	if vc:
		if vc.channel.id == channel.id:
			return
		try:
			await vc.move_to(channel)
		except asyncio.TimeoutError:
			raise VoiceConnectionError(f'Moving to channel: <{channel}> time out.')
	
	else:
		try:
			await channel.connect()
		except asyncio.TimeoutError:
			raise VoiceConnectionError(f'Connecting to channel: <{channel}> time out.')
	
	

@client.command()
async def di(ctx,*, msj):
	await ctx.send("**"+msj+"**")
	
	
client.run(TOKEN)