import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import datetime

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
	print("Bot is online!")

@client.event
async def on_message(message):
	if message.content.upper().startswith(".TEST"):
		if "%s" in [role.id for role in message.author.roles]:
			await client.send_message(message.channel, "I am awake.")
		else: 
			await client.send_message(message.channel, "zzzz")

	if message.content.upper().startswith(".PING"):
		userID = message.author.id 
		await client.send_message(message.channel,"<@%s> Hello!" % (userID))

	if message.content.upper().startswith(".SAY"):
		args = message.content.split(" ")
		await client.send_message(message.channel,"%s" % (" ".join(args[1:])))








client.run("%s")

