import discord 
from discord.ext import commands
from datetime import datetime
from token import DISCORD_TOKEN

# Bot prefix
bot = commands.Bot(command_prefix='!')

# Tasks dictionary to keep track of all the tasks
tasks = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
@bot.command()
async def createtask(ctx, assignee: discord.Member, due_date: str, *, task_description: str):
    try:
        # Parse the string into a datetime object
        due_date = datetime.strptime(due_date, '%d-%m-%Y')
        
        # Create task dictionary
        task = {
            'assignee': assignee,
            'due_date': due_date,
            'description': task_description
        }
        
        tasks[ctx.channel.id] = task
        
        # Send message in the channel
        await ctx.send(f'Task created: {task_description} | Assignee: {assignee} | Due date: {due_date}')
        
    except ValueError:
        await ctx.send('Invalid date format. Please use DD-MM-YYYY.')
        
@bot.command()
async def showtasks(ctx):
    task_list = ""
    for channel_id, task in tasks.items():
        if channel_id == ctx.channel.id:
            task_list += f"Assignee: {task['assignee']} | Due Date: {task['due_date']} | Description: {task['description']}\n"
    await ctx.send(task_list)

# Run the bot
bot.run(DISCORD_TOKEN)