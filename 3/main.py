# -*- coding: utf-8 -*-
import datetime
import <библиотека>

from <библиотека>.ext import commands
from <путь>.invite    import * # type: ignore


bot = commands.Bot(
    command_prefix = "!",
    intents        = <библиотека>.Intents.all()
)

async def punishment(bot: commands.Bot, member: <библиотека>.Member) -> None:
    try:
        channel = await member.guild.fetch_channel(0)

        await member.ban(reason = "Автобан")
        await channel.send(
            embed = <библиотека>.Embed(
                color       = <библиотека>.Color.dark_theme(), 
                title       = "Автобан", 
                description = f"**Пользователь ({member.id}) получил бан, так как дата регистрации его аккаунта не превышает минимально необходимой**"
            )
        )
    except commands.BotMissingPermissions:
        ...
    except commands.MemberNotFound:
        ...
    except commands.ChannelNotFound:
        ...
    except Exception as _:
        ...

# Задать конфиг для кога приглашений
bot.invite = InviteConfig() # type: ignore

# Время. Если время больше, чем время регистрации человека,
# то ему выдается наказание. В примере если аккаунту меньше 2 
# недель, то применяется наказание
bot.invite.time = datetime.timedelta(days = 14)

# Наказание. Наказание, выполняемое при соответствии условию
# ранней регистрации аккаунта, может быть как одним из наказаний
# на выбор: 
# InvitePunishment.NOTHING
# InvitePunishment.BAN
# InvitePunishment.KICK
# Так и асинхронной функцией, которая получает на вход бота и пользователя,
# внутри которых вы можете делать все, что хотите. Пример функции прилагается 
# выше, а ниже то, как она указывается.
# Для указания наказания на выбор просто укажите его:
# bot.invite.punishment = InvitePunishment.BAN # type: ignore
bot.invite.punishment = punishment

# Причина. Причина, которая указывается при использовании стандартных наказаний.
# Позволяет подставлять аргументы, используя:
# %member%
# %member.id%
# %member.name%
# %member.created_at%
# %member.guild%
# %member.guild.id%
# %member.guild.name%
# %guild%
# %guild.id%
# %guild.name%
# По умолчанию: "Автобан, причина: короткое время регистрации аккаунта"
bot.invite.reason = "Автобан пользователя %member.name%."
