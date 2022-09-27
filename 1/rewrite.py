@bot.slash_command(name = "угадайка", description = "Поиграйте с барменом в игру")
async def guessing(ctx: commands.Context, choice: str = commands.Param(name = 'рука', description = 'Выбирите руку левую или правую', choices = ["Левая", "Правая"])):
    teat  = random.choice(["Правая", "Левая"])
    embed = disnake.Embed(
        title = "Игра с барменом", 
        color = 0x800000
    )

    if choice == teat:
        embed.description = f"Ты выйграл, монета была в {teat[:-2].lower()}ой руке\n**Бармен растроился**"
    else:
        embed.description = f"Ты проиграл, монета была в {teat[:-2].lower()}ой руке\n**Бармен улыбнулся**"

    embed.set_footer(text = f"Запросил: {ctx.author}")
    await ctx.send(embed = embed)
