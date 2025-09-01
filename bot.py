import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

bot = commands.Bot(command_prefix='$')
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


TOKEN=os.getenv("BOT_TOKEN")
client.run(TOKEN)