import disnake
from disnake.ext import commands
from settings import token, prefix

bot = commands.Bot(command_prefix=prefix, intents=disnake.Intents().all())
bot.remove_command('help') # удаляем встроенную команду help

@bot.event # ивент, который будет нам сообщать когда бот запустился
async def on_ready():
    print("Бот запустился")


bot.run(token) # запуск бота
