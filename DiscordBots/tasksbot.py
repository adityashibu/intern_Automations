import discord
from discord import app_commands
from discord.ext import commands
from my_token import DISCORD_TOKEN

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is up and ready")
    try: 
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
        
@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!", ephemeral=True)
    
@bot.tree.command(name="name")
async def name(interaction:discord.Interaction):
    await interaction.response.send_message(f"Your name is {interaction.user.mention}!")

bot.run(DISCORD_TOKEN)