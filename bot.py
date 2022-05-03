import os, random, time

import discord, asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await asyncio.sleep(300)
    guild = client.guilds[0]
    await random.choice(guild.text_channels).send("Quack")



@client.event
async def on_message(message):
    if (random.randint(0, 100) == 1) and (message.author != client.user):
        await message.channel.send("Quack")
    if message.author == client.user:
        return
    message_split = message.content.split(' ')
    count = 0
    random_chance = random.randint(1, 100)
    if random_chance == 1:
        pass
    elif message.content == '🍞' or message.content == "bread":
        await message.delete()
        response = "haha stole your :bread:"
        await message.channel.send(response)
        cooldown = True
    else:
        for item in message_split:
            count += 1
            if item == "bread" or item == '🍞':
                message_backup = message.content
                channel = message.channel
                await message.delete()
                response = "haha stole your :bread:, keep in mind that my mouth can only fit 1 slice"
                response2 = "anyway here is the message without 🍞"
                message_no_bread = list(filter(lambda x: x != {item}, str(message_backup).split()))
                await message.channel.send(response)
                await message.channel.send(response2)
                await message.channel.send(message_no_bread)
                break










client.run(TOKEN)