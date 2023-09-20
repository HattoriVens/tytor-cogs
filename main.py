import disnake
from disnake.ext import commands
from settings import token, prefix
import os

bot = commands.Bot(command_prefix=prefix, intents=disnake.Intents().all())
bot.remove_command('help') # удаляем встроенную команду help

@bot.event # ивент, который будет нам сообщать когда бот запустился
async def on_ready():
    print("Бот запустился")

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run(token) # запуск бота
