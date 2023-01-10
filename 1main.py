import os
import discord 
from random import *

import MysteryCharacter as mei
mysterycharacterultcharge = ''
import KianaKaslana as kiana
import blade as bladie
import BronyaRand as bronra
import Elysia as ellie
import amonsters as mons

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

enemy1 = []
enemy2 = []
enemy3 = []
class Client:
    def event(self, func):               
        if func.__name__ == "on_message":
            self.on_message_handle = func
            return func

    def receive_message(self, msg):
        func = getattr(self, "on_message_handle", None)
        if func is not None:
            func(msg)
        else:
            self.process_commands(msg)

@client.event 
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message, arg1, arg2):
    if message.content.lower().startswith("mystery"):
        #mysterycharacter
        print("hi")
    if message.content.lower().startswith("kiana"):
        #kiana
        print("hello world")
    if message.content.lower().startswith("blade"):
        #blade
        print("blade")
    if message.content.lower().startswith("bronyarand"):
        #bronya rand
        print("bronya rand")
    if message.content.lower().startswith("elysia"):
        #elysia 
        print("elysia")
        
client.run("MTA0NDgwMjU4ODMyNDkzMzcwMw.G1EPVJ.TzOyY2uGWw12QXGp2civRKjO9fPNTC3YCJkaqE")
