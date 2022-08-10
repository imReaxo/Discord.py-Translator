#----------Imports & Froms----------#
import discord
from discord.ext import commands
from googletrans import Translator
#----------Imports & Froms----------#

#---------Complete this-------#
TOKEN = "Your bot token"
PREFIX = "Your bot prefix"
#---------Complete this-------#

#----------Clients & On ready------#
client=commands.Bot(command_prefix=PREFIX)

@client.event
async def on_ready():
    print("bot is ready")
#----------Client & On ready------#


#----------Code--------#
@client.command()
async def translate(ctx, lan, *, text):
    translator = Translator()
    translation = translator.translate(text, dest=lan)
    embed = discord.Embed(title=":blue_book: Translated :blue_book:",description=f"{translation.text}",color=discord.Color.dark_blue())
    embed.set_footer(text=f"Detect language ----> {lan}")
    await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please complete your message! **{PREFIX}translate (language) (text)**")

#----------Code--------#


#-------run-------#
client.run(TOKEN)
#-------run-------#