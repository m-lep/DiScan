from email import message
import requests 
from bs4 import BeautifulSoup 
from discord.ext.commands import Bot  
import discord
import os
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import commands
load_dotenv()

bot = commands.Bot(command_prefix="$")
client=commands.Bot(command_prefix="$")





@client.event
async def on_ready():
    print('We have logged in as {}'.format(client))

def getdata(url): 
    r = requests.get(url) 
    return r.text 






@bot.event
async def on_message(message):
	if message.content == "hello":
		await message.channel.send("pies are better than cakes. change my mind.")
	await bot.process_commands(message)

@bot.command(
	help="Uses come crazy logic to determine if pong is actually the correct value or not.",
	brief="Prints pong back to the channel."
)

async def scan(ctx):
    embed = discord.Embed(title="📖 - Choisis le manga que tu souhaites lire en scan", description="🔰 > Attaque Des Titans\n 👶🏻 > Beelzebub\n 🍀 > Black Clover\n 👻 > Bleach", color=0x00ff00)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("🔰")
    await msg.add_reaction("👶🏻")
    await msg.add_reaction("🍀")
    await msg.add_reaction("👻")
    #var1 = ctx.channel.fetch_message(message.id)


@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message.author != user:
        if reaction.message.author.id == 934789863687999508:
            if '📖' in reaction.message.embeds[0].title:
                channel = reaction.message.channel
                await channel.send("{} has added {} to the message".format(user.name, reaction.emoji))


async def print(ctx, *args):
	response = ""
	for arg in args:
		response = response + " " + arg
	await ctx.channel.send(response)

@bot.command()
async def skin(ctx, arg1, arg2):
    htmldata = getdata("https://www.frscan.cc/manga/one-punch-man/{}/{}".format(arg1, arg2))
    soup = BeautifulSoup(htmldata, 'html.parser') 
    for item in soup.find_all('img', class_="img-responsive scan-page"):     
        embed = discord.Embed(title="One Punch Man", description="Chapitre {}, Page {}".format(arg1, arg2), color=0x00ff00) #creates embed
        embed.set_image(url=item['src'])
        msg = await ctx.channel.send(embed=embed)
        await msg.add_reaction("✅")

bot.run("OTM0Nzg5ODYzNjg3OTk5NTA4.Ye1M5w.5oyL1ASbgBs_olNI9F6uoJkhcCE")




