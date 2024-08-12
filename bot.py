import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Get the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

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
    welcome_channel = discord.utils.get(guild.text_channels, name='guardian-welcome')  # Ensure you have a channel named 'guardian-welcome'
    if welcome_channel:
        await welcome_channel.send(f'Welcome to the server, {member.mention}!')

@bot.event
async def on_disconnect():
    print('Bot has been disconnected.')

@bot.event
async def on_connect():
    print('Bot has reconnected.')

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

# Command to generate a random number between a given range
@bot.command(name='random')
async def random_number(ctx, min: int, max: int):
    if min > max:
        await ctx.send("The minimum value cannot be greater than the maximum value.")
        return

    number = random.randint(min, max)
    await ctx.send(f'Your random number between {min} and {max} is: {number}')

# Run the bot with your token
bot.run(TOKEN)
