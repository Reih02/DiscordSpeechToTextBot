import os
import random
import discord
import time

TOKEN = 'ENTER TOKEN HERE'

client = discord.Client()

f = open('speech.txt', 'r')
check = f.read()

a = 0

@client.event
async def on_ready():
    print('{} is online and operational'.format(client.user))

@client.event
async def on_message(message):
    if message.content == 'speak':
        a = 0
        while a < 1:
            f = open('speech.txt', 'r')
            speech = f.read()
            if speech != check and speech != "":
                response = (speech)
                await message.channel.send(response)
                f = open('speech.txt', 'r')
                check1 = f.read()
                a = a + 1

        while a >= 1:
            f = open('speech.txt', 'r')
            speech = f.read()
            if speech != check1 and speech != "":
                response = (speech)
                await message.channel.send(response)
                f = open('speech.txt', 'r')
                check1 = f.read()

client.run(TOKEN)
