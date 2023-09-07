import os
import datetime
import random
import urllib, json
import discord
from discord.ext import tasks, commands
import keep_alive

keep_alive.keep_alive()

Token = os.environ['Token']

client = commands.Bot(command_prefix='-')

Prayer_Times = 'a'

#Do Prayer Times Get Request:
format = 'http://www.londonprayertimes.com/api/times/?format=json'
today = '&date=' + str(datetime.date.today())
API_Key = os.environ['API_Key']
key = '&key='+API_Key
hour_format = '&24hours=true'
link = format+key+today+hour_format
response = urllib.request.urlopen(link)
Prayer_Times = json.loads(response.read())

@client.event
async def on_ready():
	print('Bot Is Online')

@client.command()
async def times(ctx):
	await ctx.message.delete()
	format = 'http://www.londonprayertimes.com/api/times/?format=json'
	today = '&date=' + str(datetime.date.today())
	API_Key = os.environ['API_Key']
	key = '&key='+API_Key
	hour_format = '&24hours=true'
	link = format+key+today+hour_format
	response = urllib.request.urlopen(link)
	Prayer_Times = json.loads(response.read())
	
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	
	embed=discord.Embed(title='Prayer Times', color=discord.Color.from_rgb(r,g,b))
	embed.add_field(name = 'Date', value = Prayer_Times['date'] , inline = False)
	embed.add_field(name = 'City', value = Prayer_Times['city'] , inline = False)
	embed.add_field(name = 'Fajr', value = Prayer_Times['fajr'] , inline = False)
	embed.add_field(name = 'Zuhr', value = Prayer_Times['dhuhr'] , inline = False)
	embed.add_field(name = 'Asr', value = Prayer_Times['asr'] , inline = False)
	embed.add_field(name = 'Maghrib', value = Prayer_Times['magrib'] , inline = False)
	embed.add_field(name = 'Isha', value = Prayer_Times['isha'] , inline = False)
	embed.set_footer(text='Requested By: ' + str(ctx.author))
	
	await ctx.send(embed=embed)

@tasks.loop(seconds=60)
async def Time_Check(Prayer_Times):
	Now = datetime.datetime.now()
	if str(Now.hour) == '23':
		a = '00'
	else:
		a = str(int(Now.hour) + 1)
	if len(a) == 1:
		a = '0' + a
	b = ':'
	if len(str(Now.minute)) ==1:
		c = '0'+str(Now.minute)
	else:
		c = str(Now.minute)
	Current_Time = a + b + c
	print(Current_Time)
	if str(Prayer_Times['fajr']) == Current_Time:
		await client.get_channel(842865013387165707).send("**<@&982286166286028800> It's Fajr Time**")
		await client.get_channel(982767431820918884).send("**<@&982767101490118696> It's Fajr Time**")
		await client.get_channel(988558234891722852).send("**<@&988558591692783616> It's Fajr Time**")
	elif str(Prayer_Times['dhuhr']) == Current_Time:
		await client.get_channel(842865013387165707).send("**<@&982286166286028800> It's Zuhr Time**")
		await client.get_channel(982767431820918884).send("**<@&982767101490118696> It's Zuhr Time**")
		await client.get_channel(988558234891722852).send("**<@&988558591692783616> It's Zuhr Time**")
	elif str(Prayer_Times['asr']) == Current_Time:
		await client.get_channel(842865013387165707).send("**<@&982286166286028800> It's Asr Time**")
		await client.get_channel(982767431820918884).send("**<@&982767101490118696> It's Asr Time**")
		await client.get_channel(988558234891722852).send("**<@&988558591692783616> It's Asr Time**")
	elif str(Prayer_Times['magrib']) == Current_Time:
		await client.get_channel(842865013387165707).send("**<@&982286166286028800> It's Maghrib Time**")
		await client.get_channel(982767431820918884).send("**<@&982767101490118696> It's Maghrib Time**")
		await client.get_channel(988558234891722852).send("**<@&988558591692783616> It's Maghrib Time**")
	elif str(Prayer_Times['isha']) == Current_Time:
		await client.get_channel(842865013387165707).send("**<@&982286166286028800> It's Isha Time**")
		await client.get_channel(982767431820918884).send("**<@&982767101490118696> It's Isha Time**")
		await client.get_channel(988558234891722852).send("**<@&988558591692783616> It's Isha Time**")
	if '01:01' == Current_Time:
		today = '&date=' + str(datetime.date.today())
		link = format+key+today+hour_format
		response = urllib.request.urlopen(link)
		Prayer_Times = json.loads(response.read())

		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)

		embed=discord.Embed(title='Prayer Times', color=discord.Color.from_rgb(r,g,b))
		embed.add_field(name = 'Date', value = Prayer_Times['date'] , inline = False)
		embed.add_field(name = 'City', value = Prayer_Times['city'] , inline = False)
		embed.add_field(name = 'Fajr', value = Prayer_Times['fajr'] , inline = False)
		embed.add_field(name = 'Zuhr', value = Prayer_Times['dhuhr'] , inline = False)
		embed.add_field(name = 'Asr', value = Prayer_Times['asr'] , inline = False)
		embed.add_field(name = 'Maghrib', value = Prayer_Times['magrib'] , inline = False)
		embed.add_field(name = 'Isha', value = Prayer_Times['isha'] , inline = False)
		await client.get_guild(745577737263120404).get_channel(842865013387165707).send(embed=embed)
		await client.get_guild(677249774918828074).get_channel(982767431820918884).send(embed=embed)
		await client.get_guild(763125993719595089).get_channel(988558234891722852).send(embed=embed)
	#elif '22:51' == Current_Time:
		#await client.get_channel(988558234891722852).send("**<@&988558591692783616> Debug**")
		
@client.command()
async def say(ctx, *, text):
	if ctx.message.author.id == 370594904268734464:
		await ctx.message.delete()
		await ctx.send(f"{text}")
	else:
		await ctx.send('Command Restricted To Bot Owner')

@client.command()
async def ping(ctx):
	await ctx.send(f'My ping is {round(client.latency*1000, 2)} ms!')

Time_Check.start(Prayer_Times)
client.run(Token)