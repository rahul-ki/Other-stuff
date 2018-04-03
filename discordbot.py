import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "!") #Initialise client bot


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
#use upper() on every message to remove the problem of case sensitivity.
    greetings = ["HI", "HELLO", "HOLA", "HEY", "HEYY"]
    tokens = message.content.split(" ")
    if tokens[0].upper() in greetings :
        userID = message.author.id  #user ID
        await client.send_message(message.channel,"<@%s> Hey! What can I do for you?" % (userID))
# await as we need to wait for user to type something.
#@ tags the user. %s is the user id

    elif message.content.upper() == "CAN I GET FREE HOME DELIVERY?":
        await client.send_message(message.channel, '''
Free standard home delivery on orders over £50 - get your clothing, home, beauty and wine order within 3-5 working days. 

Free standard home delivery on hampers orders over £20.

Plus, if you spend over £100 on wine you'll get free named day delivery.

From time to time we do run delivery promotions in our marketing emails – sign up to our newsletter to keep up to date.

Please note, the delivery charge is deducted in the checkout. You must select the £3.50 standard delivery, then check your summary for the discount.
''')

    elif message.content.upper() == "HOW DO I FIND OUT THE OPENING TIMES, ADDRESSES AND FACILITIES FOR M&S STORES IN THE UK?" :
        await client.send_message(message.channel, '''Our store information varies. Please go to this link: 
https://www.marksandspencer.com/webapp/wcs/stores/servlet/MSResStoreFinderGlobalBaseCmd?storeId=10151&langId=-24&catalogId=10051&krypto=RnJ3oP2BdMZ616BjHqg1GpDdqCqJ18v08vWPweYRvaX1abPtIpk5O2bRfEkiTeiJVjpAa6dyW2t4xOyix794l%2FW5p%2BDn80bORM3y%2B7e1t353vAEd6LB60%2BcV3M5%2F59h3&ddkey=http%3AMSStoreFinderGlobalBaseView
''')
    elif message.content.upper() == "CAN I USE PAYPAL?" :
        await client.send_message(message.channel, "At the current time you cannot use PayPal on marksandspencer.com.")
    
# deleting messages:-
'''
@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** You're not allowed to use that word here!")
                except discord.errors.NotFound:
                    return
'''					
client.run("MzkxMzExMjQwMDYyMDQyMTM0.DZL8uQ.CPFgYRKdhqqBbaipLrD4-UQy0xk") #TO actually run the bot.
