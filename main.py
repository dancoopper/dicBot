import disnake
from disnake.ext import commands
from disnake import *
import apod_object_parser
import nasapy

intents = disnake.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(test_guilds=[123456])

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.slash_command()
async def ping(inter):
    """Pings the bot and if the bot if up it will respond with 'pong'"""
    await inter.response.send_message("Pong")



@bot.slash_command()
async def add(inter: disnake.AppCmdInter, left: int, right: int):
    """Adds two numbers together."""
    await inter.response.send_message(left + right)


@bot.slash_command()
async def ponko(intern:disnake.AppCmdInter):
    
        response = apod_object_parser.get_data(API KEY HERE)
        date = apod_object_parser.get_date(response)
        url = apod_object_parser.get_url(response)
        apod_object_parser.download_image(url, date)
        apod_object_parser.convert_image(f"pics\\{date}.jpg")
        await intern.channel.send("Title: " + apod_object_parser.get_title(response))
        await intern.channel.send(file=disnake.File(f"pics\\{date}.png"))
        await intern.channel.send("Explanination: " + apod_object_parser.get_explaination(response))
        


@bot.slash_command()
async def nasa(inter:disnake.AppCmdInter, date):
        """gets pic of the day for any date after like 1990"""
        try:
            n = nasapy.Nasa(API KEY HERE)
            response = n.picture_of_the_day(date, False)
            url = apod_object_parser.get_url(response)
            apod_object_parser.download_image(url, date)
            apod_object_parser.convert_image(f"pics\\{date}.jpg")
            await inter.channel.send(file=disnake.File(f"pics\\{date}.png"))
            
        except:
            await inter.response.send_message("something went wrong tbh man idk if you should even try with this anymore")


@bot.slash_command()
async def help(inter:disnake.AppCmdInter):
    

    embed =disnake.Embed(color= disnake.Color.blue())
    embed.set_author(name = "Help")
    embed.add_field(name="/ponko", value="sends the nasa pic of the day and a lil info on it", inline=False)
    embed.add_field(name="/nasa", value="sends the nasa pic of the day from any date you want", inline=False)
    embed.add_field(name="/ping", value="pings the bot to see if it's working", inline=False)
    embed.add_field(name="/add", value="adds to numbers...idk man I was out of ideas", inline=False)
    await inter.response.send_message(embed=embed)

bot.run(TOKEN HERE)
