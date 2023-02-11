import disnake
from disnake.ext import commands
import requests
import hmtai
import random
from config import *
import json

class nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="nsfw",
        description="Nsfw anime pics",
        options=[
            disnake.Option(
                name="genre",
                description="Which nsfw command do you want run?",
                required=True, 
                type=disnake.OptionType.string,
                choices=[
                    disnake.OptionChoice(name="Anal", value="anal"),
                    disnake.OptionChoice(name="Ass", value="ass"),
                    disnake.OptionChoice(name="Boobs", value="boobs"),
                    disnake.OptionChoice(name="Bdsm", value="bdsm"),
                    disnake.OptionChoice(name="B-job", value="blowjob"),
                    disnake.OptionChoice(name="Cum", value="cum"),
                    disnake.OptionChoice(name="Feet", value="feet"),
                    disnake.OptionChoice(name="Femdom", value="femdom"),
                    disnake.OptionChoice(name="Hentai", value="hentai"),
                    disnake.OptionChoice(name="Hentai gifs", value="hentaigif"),
                    disnake.OptionChoice(name="Incest", value="incest"),
                    disnake.OptionChoice(name="Kuni", value="kuni"),
                    disnake.OptionChoice(name="Manga", value="manga"),
                    disnake.OptionChoice(name="Masturbation", value="masturbation"),
                    disnake.OptionChoice(name="Masturbation gifs", value="masturbationgif"),
                    disnake.OptionChoice(name="Neko", value="neko"),
                    disnake.OptionChoice(name="Neko gifs", value="nekogif"),
                    disnake.OptionChoice(name="Orgy", value="orgy"),
                    disnake.OptionChoice(name="Orgy gifs", value="orgygif"),
                    disnake.OptionChoice(name="Succubs", value="succubs"),
                    disnake.OptionChoice(name="Tentacles", value="tentacles"),
                    disnake.OptionChoice(name="Thighs", value="thighs"),
                    disnake.OptionChoice(name="Uniform", value="uniform"),
                    disnake.OptionChoice(name="Yuri", value="yuri"),
                    disnake.OptionChoice(name="Yuri gifs", value="yurigif")
                ]
            ),
            disnake.Option(
                name="amount",
                description="The number of pictures the bot will send",
                required=False,
                type=disnake.OptionType.integer
            )
        ],
        
    )
    @commands.guild_only()
    @commands.is_nsfw()
    @commands.cooldown(1, 8, commands.BucketType.member)
    async def nsfw(self, ctx, genre, amount=1):
        with open('database/landb.json', 'r') as f: ldb = json.load(f)
        with open('language/lang.json', 'r', encoding='utf-8') as f: lan = json.load(f)
        lancode = ldb[str(ctx.guild.id)]
        if amount > 10:
            embed = disnake.Embed(title=f"{lan[lancode]['error']} <a:vx:903378126942380073>", description=f"**{lan[lancode]['errornsfwtoomuch']}**", colour=errorcolor)
            await ctx.response.send_message(embed=embed, ephemeral=True)
        else:
            if genre == "anal":
                for i in range(amount):
                    number = random.randint(1,3)
                    if number == 1:
                        req = requests.get("https://purrbot.site/api/img/nsfw/anal/gif")
                        res = req.json()
                        hentai = res['link']
                    if number == 2:
                        hentai = hmtai.get("nekobot","hanal")
                    else:
                        hentai = hmtai.get("hmtai","anal")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwanal']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "ass":
                for i in range(amount):
                    number = random.randint(1,2)
                    if number == 1:
                        hentai = hmtai.get("hmtai","ass")
                    else:
                        hentai = hmtai.get("nekobot","hass")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwass']}")
                    await ctx.send(embed=embed)
                    
            
            elif genre == "bdsm":
                for i in range(amount):
                    hentai = hmtai.get("hmtai","bdsm")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwbdsm']}")
                    await ctx.send(embed=embed)
                    
            
            elif genre == "blowjob":
                for i in range(amount):
                    number = random.randint(1,2)
                    if number == 1:
                        hentai = hmtai.get("hmtai","blowjob")
                    else:
                        hentai = hmtai.get("hmtai","boobjob")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwblowjob']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "cum":
                for i in range(amount):
                    number = random.randint(1,2)
                    if number == 1:
                        hentai = hmtai.get("hmtai","cum")
                    else:
                        hentai = hmtai.get("hmtai","creampie")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwcum']}")
                    await ctx.send(embed=embed)



            elif genre == "feet":
                for i in range(amount):
                    hentai = hmtai.get("hmtai","footjob")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwfeet']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "femdom":
                for i in range(amount):
                    hentai = hmtai.get("hmtai","femdom")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwfemdom']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "boobs":
                for i in range(amount):
                    hentai = hmtai.get("hmtai","boobs")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwboobs']}")
                    await ctx.send(embed=embed)


            elif genre == "hentai":
                for i in range(amount):
                    number = random.randint(1,3)
                    if number == 1:
                        hentai = hmtai.get("hmtai","hentai")
                    else:
                        hentai = hmtai.get("nekobot","hentai")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwhentai']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "hentaigif":
                for i in range(amount):
                    number = random.randint(1,2)
                    if number == 1:
                        hentai = hmtai.get("hmtai","gif")
                    else:
                        hentai = hmtai.get("hmtai","classic")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwhentaigif']}")
                    await ctx.send(embed=embed)


            elif genre == "incest":
                await ctx.send(f"{lan[lancode]['nsfwincest']}")
                for i in range(amount):
                    hentai = hmtai.get("hmtai","incest")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwincest']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "kuni":
                for i in range(amount):
                    req = requests.get("https://purrbot.site/api/img/nsfw/pussylick/gif")
                    res = req.json()
                    hentai = res['link']
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwkuni']}")
                    await ctx.send(embed=embed)


            elif genre == "manga":
                for i in range(amount):
                    hentai = hmtai.get("hmtai","manga")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwmanga']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "neko":
                for i in range(amount):
                    number = random.randint(1,3)
                    if number == 1:
                        req = requests.get("https://purrbot.site/api/img/nsfw/neko/img")
                        res = req.json()
                        hentai = res['link']
                    elif number == 2:
                        hentai = hmtai.get("nekobot","nekolewd")
                    else:
                        hentai = hmtai.get("nekobot","hneko")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwneko']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "nekogif":
                for i in range(amount):
                    number = random.randint(1,2)
                    if number == 1:
                        req = requests.get("https://purrbot.site/api/img/nsfw/neko/gif")
                        res = req.json()
                        hentai = res['link']
                    else:
                        hentai = hmtai.get("nekos","nekogif")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwnekogif']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "orgy":
                for i in range(amount):
                    hentai = hmtai.get("hmtai","orgy")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfworgy']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "orgygif":
                for i in range(amount):
                    responses = [
                        "https://purrbot.site/api/img/nsfw/threesome_mmf/gif",
                        "https://purrbot.site/api/img/nsfw/threesome_ffm/gif",
                        "https://purrbot.site/api/img/nsfw/threesome_fff/gif"
                    ]
                    response = random.choice(responses)
                    req = requests.get(response)
                    res = req.json()
                    hentai = res['link']
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfworgygif']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "uniform":
                for i in range(amount):
                    hentai = hmtai.get("hmtai","uniform")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwuniform']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "masturbation":
                for i in range(amount):
                    hentai = hmtai.get("hmtai","masturbation")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwmasturbation']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "masturbationgif":
                for i in range(amount):
                    req = requests.get("https://purrbot.site/api/img/nsfw/solo/gif")
                    res = req.json()
                    hentai = res['link']
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwmasturbationgif']}")
                    await ctx.send(embed=embed)


            elif genre == "succubs":
                for i in range(amount):
                    hentai = hmtai.get("hmtai","succubs")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwsuccubs']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "tentacles":
                for i in range(amount):
                    hentai = hmtai.get("hmtai","tentacles")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwtentacles']}")
                    await ctx.send(embed=embed)

            elif genre == "thighs":
                for i in range(amount):
                    hentai = hmtai.get("hmtai","thighs")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwthighs']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "yuri":
                for i in range(amount):
                    number = random.randint(1,2)
                    if number == 1:
                        hentai = hmtai.get("hmtai","yuri")
                    else:
                        hentai = hmtai.get("nekobot","yuri")
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwyuri']}")
                    await ctx.send(embed=embed)
                    

            elif genre == "yurigif":
                await ctx.send(f"{lan[lancode]['nsfwyurigif']}")
                for i in range(amount):
                    req = requests.get("https://purrbot.site/api/img/nsfw/yuri/gif")
                    res = req.json()
                    hentai = res['link']
                    embed = disnake.Embed(color=0x2f3136)
                    embed.set_image(url=hentai)
                    embed.set_footer(text=f"{lan[lancode]['nsfwyuri']}")
                    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(nsfw(bot))
