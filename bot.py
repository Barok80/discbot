import discord
from discord.ext import commands

# Replace 'your_token_here' with your bot's token
TOKEN = 'MTI1OTk4ODAyNTIzMjg1NTA1MQ.G4qqiy.9ehIsdlxO_cPAu0ODQZaP1OvGyTkywIIwyD7AY'

# Set up the bot
intents = discord.Intents.default()
intents.members = True  # Enable the members intent
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    guild = member.guild
    welcome_channel = discord.utils.get(guild.text_channels, name='guardian-welcome')  # Ensure you have a channel named 'welcome'
    if welcome_channel:
        await welcome_channel.send(f'Welcome to the server, {member.mention}!')

bot.run(TOKEN)
