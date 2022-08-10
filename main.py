@bot.slash_command(
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
                disnake.OptionChoice(name="Bdsm", value="bdsm"),
                disnake.OptionChoice(name="Blowjob", value="blowjob"),
                disnake.OptionChoice(name="Cum", value="cum"),
                disnake.OptionChoice(name="Feet", value="feet"),
                disnake.OptionChoice(name="Femdom", value="femdom"),
                disnake.OptionChoice(name="Hentai", value="hentai"),
                disnake.OptionChoice(name="Hentai gifs", value="hentaigif"),
                disnake.OptionChoice(name="Kuni", value="kuni"),
                disnake.OptionChoice(name="Neko", value="neko"),
                disnake.OptionChoice(name="Neko gifs", value="nekogif"),
                disnake.OptionChoice(name="Orgy", value="orgy"),
                disnake.OptionChoice(name="Orgy gifs", value="orgygif"),
                disnake.OptionChoice(name="School", value="school"),
                disnake.OptionChoice(name="Solo", value="solo"),
                disnake.OptionChoice(name="Solo gifs", value="sologif"),
                disnake.OptionChoice(name="Succubs", value="succubs"),
                disnake.OptionChoice(name="Thighs", value="thighs"),
                disnake.OptionChoice(name="Yuri", value="yuri"),
                disnake.OptionChoice(name="Yuri gifs", value="yurigif"),
                disnake.OptionChoice(name="Yaoi", value="yaoi"),
                disnake.OptionChoice(name="Yaoi gifs", value="yaoigif"),
                disnake.OptionChoice(name="Raddon NSFW pic", value="rpic")
            ]
        ),
        disnake.Option(
            name="amount",
            description="Amount of nsfw pics",
            required=False,
            type=disnake.OptionType.integer
        )
    ],
    
)
@commands.guild_only()
@commands.is_nsfw()
async def nsfw(ctx, genre):
        if genre == "anal":
            req = requests.get("https://purrbot.site/api/img/nsfw/anal/gif")
            res = req.json()
            await ctx.send(res['link'])

        elif genre == "ass":
            await ctx.send(akaneko.nsfw.ass())
        
        elif genre == "bdsm":
            await ctx.send(akaneko.nsfw.bdsm())
        
        elif genre == "blowjob":           
            await ctx.send(akaneko.nsfw.blowjob())

        elif genre == "cum":             
            req = requests.get("https://purrbot.site/api/img/nsfw/cum/gif")
            res = req.json()
            await ctx.send(res['link'])

        elif genre == "feet":            
            await ctx.send(akaneko.nsfw.feet())

        elif genre == "femdom":
            await ctx.send(akaneko.nsfw.femdom())

        elif genre == "hentai":
            await ctx.send(akaneko.nsfw.hentai())

        elif genre == "hentaigif":
            await ctx.send(akaneko.nsfw.gif())

        elif genre == "kuni":
            req = requests.get("https://purrbot.site/api/img/nsfw/pussylick/gif")
            res = req.json()
            await ctx.send(res['link'])

        elif genre == "neko":
            req = requests.get("https://purrbot.site/api/img/nsfw/neko/img")
            res = req.json()
            await ctx.send(res['link'])

        elif genre == "nekogif":
            req = requests.get("https://purrbot.site/api/img/nsfw/neko/gif")
            res = req.json()
            await ctx.send(res['link'])

        elif genre == "orgy":
            await ctx.send(akaneko.nsfw.orgy())

        elif genre == "orgygif":
            responses = [
                "https://purrbot.site/api/img/nsfw/threesome_mmf/gif",
                "https://purrbot.site/api/img/nsfw/threesome_ffm/gif",
                "https://purrbot.site/api/img/nsfw/threesome_fff/gif"
            ]
            response = random.choice(responses)
            req = requests.get(response)
            res = req.json()
            await ctx.send(res['link'])

        elif genre == "school":
            await ctx.send(akaneko.nsfw.school())

        elif genre == "solo":
            await ctx.send(akaneko.nsfw.masturbation())

        elif genre == "sologif":
            req = requests.get("https://purrbot.site/api/img/nsfw/solo/gif")
            res = req.json()
            await ctx.send(res['link'])

        elif genre == "succubs":
            await ctx.send(akaneko.nsfw.succubus())

        elif genre == "thighs":
            await ctx.send(akaneko.nsfw.thighs())

        elif genre == "yuri":             
            await ctx.send(akaneko.nsfw.yuri())

        elif genre == "yurigif":
            req = requests.get("https://purrbot.site/api/img/nsfw/yuri/gif")
            res = req.json()
            await ctx.send(res['link'])

        elif genre == "yaoi":
            req = requests.get("http://38.101.26.74/api/v1/yaoi")
            res = req.json()
            await ctx.send(res['url'])

        elif genre == "yaoigif":
            req = requests.get("http://38.101.26.74/api/v1/gifs")
            res = req.json()
            await ctx.send(res['url'])

        elif genre == "rpic":
            await ctx.send(" ".join(akaneko.nsfw.lewdbomb(1)))
