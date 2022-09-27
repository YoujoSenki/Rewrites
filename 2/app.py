# -*- coding: utf-8 -*-
import disnake
import datetime

from disnake.ext import commands


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        # Инициализация класса, передает все
        # полученные аргументы в наследуемый
        # класс бота
        super().__init__(*args, **kwargs)
        
    async def start(self, *args, **kwargs) -> None:
        # В данном месте вы можете заносить разные переменные
        # в класс бота для дальнейшего использования их в когах/командах
        # и т.п.

        # Для примера укажу время запуска бота
        self.start_up = datetime.datetime.now()

        # Передает все для запуска бота
        await super().start(*args, **kwargs)
    
    async def close(self) -> None:
        # В основном не нужная вещь, но если вы используете
        # конфиги, базы данных и т.п. с открытием сессий через
        # async def start, то тут вы можете это все закрывать

        # А это просто отключалка бота,
        # и да я знаю, что она спамит в консоль
        try:    
            await super().close()

            # Если вам не нравится спам в консоли при выключении бота,
            # то можете раскоментировать эти строки, но не забудьте
            # импортировать библиотеку os:

            # if os.name == 'nt':
            #     os.system("cls")
            # else:
            #     os.system("clear")

            quit()
        except: 
            pass

# Ког для примера
class Cog(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.command(name = 'тест')
    async def test(self, ctx: commands.Context) -> None:
        # Использование переменной записанной в async def start
        await ctx.send(f"Бот запущен с: {self.bot.start_up}")

async def prefix(bot: Bot, message: disnake.Message) -> None:
    # В этой функции вы можете прописать получение 
    # префиксов из конфига под любой конкретный сервер/группу серверов
    # да и вообще по вашему полному желанию
    #
    # Функция асинхронная, так что вы можете мутить здесь и с
    # асинхронными базами данных на здоровье

    # Избежание ошибок при отсутствии сервера,
    # если сервера нет - возвращает стандартный префикс 
    if message.guild == None:
        return "?"

    # Здесь вы можете уже писать любой алгоритм получения префикса
    # можете хоть конфиг/бд пихать в бота и использовать через 
    # bot.переменная_базы_данных и т.п.
    return "?"

client = Bot(
    # Отсылка к функции, в которой вы можете прописать 
    # любой способ получения префикса, изменения его для 
    # отдельных серверов и так далее
    command_prefix = prefix, 
    # Изменяете разрешения по своему вкусу, 
    # я по умолчанию ставлю все
    intents        = disnake.Intents.all(), 
    # help_command   = None # Если вы хотите убрать дефолтную комнаду help
)

# Добавление тестового кога
client.add_cog(Cog(client))
# Запуск бота
client.run("MTAxMTY4MDg5OTA4NTExMTM4Ng.GlJuXb.O-xVf-7H2wdK448NtdqulIs6GcE4MgR8F8wX9c")