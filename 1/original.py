qa =["Правой", "Левой"]
     
@bot.slash_command(name="ugadai", description = "Поиграйте с барменом в игру ")
async def ugadai(ctx, ruka: str = commands.Param (name='рука', description='Выбирите руку левую или правую', choices=["Левой", "Правой"])):
    teat = random.choice(qa)
    if ruka == teat:
     embed=disnake.Embed(
     title="Игра с барменом", 
     description=f"Ты выйграл, монета была в {teat} руке \n**Бармен растроился**", color=0x800000)
     embed.set_footer(text=f"Запросил {ctx.author}")
     await ctx.send(embed=embed)
    else:
     embeed=disnake.Embed(
     title="Игра с барменом", 
     description=f"Ты проиграл, монета была в {teat} руке \n**Бармен улыбнулся** ", color=0x800000)
     embeed.set_footer(text=f"Запросил {ctx.author}")
     await ctx.send(embed=embeed)
