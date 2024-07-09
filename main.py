import discord
from discord.ext import commands
from modelRunner import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')

@bot.command(name="hello")
async def hello(ctx):
  await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command(name="check") 
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f"./{file_name}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")


bot.run("MyToken")
