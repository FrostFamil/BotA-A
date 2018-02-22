import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot Hazirdi!")

chat_filter = ["OGRAS", "GOT", "CINDIR", "GOTVEREN", "POX", "QEHBE"]
bypass_list = []


@client.event
async def on_message(message):
    if message.content.upper().startswith('SALAM'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Salam :grinning:" % (userID))

    elif message.content.upper().startswith('NECESEN'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Belede Salamatciligdi sen necesen ? :wink:" % (userID))
    
    elif message.content.upper().startswith('!SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        
    elif message.content.upper().startswith('!ADMIN'):
        if "193078142095720448" in (role.id for role in message.author.roles):
            await client.send_message(message.channel, "Adminsen!!!")
        else:
            await client.send_message(message.channel, "Admin Deyilsen")
    
    elif message.content.upper().startswith('!BOT'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Ala Menemde Botlarin Sevimlisi BotAga" % (userID))

    elif message.content.upper().startswith('VEZYET'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Belede Salamatciligdi Yavas Yavas firranirig :wink:" % (userID))

    elif message.content.upper().startswith('NECE YASIN VAR'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Brat Botun Yasi Olmur :sunglasses:" % (userID))


@client.event
async def on_message(message):
    userID = message.author.id
    contents = message.content.split(" ") 
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.send_message(message.channel, "<@%s> Aye A gede Soyus soyme ayibdi :grinning:" % (userID))
                except discord.errors.NotFound:
                    return



client.run("NDE0OTIwMTQ1ODExNTM3OTIx.DWurWQ.vxRaGVazOtO7W_ZUVt03Fp8B4O8")



