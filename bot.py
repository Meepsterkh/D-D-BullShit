
from discord.ext.commands import Bot
from discord import Game
import discord
from spellAPI import*
import random
import requests


# def main settings
prefix = ("|")
token = 'NTI1ODU1MzIxNjIxNTI4NTk3.Dv9Obg.p7AYaFboWFwVaHRsqXKmX1i4oRc'

# change main settings
client = Bot(command_prefix=prefix)
client.remove_command("help")


# Program start up
@client.event
async def on_ready():
    await client.change_presence(game = Game(name = "with spells... write \"|help\" to start"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# function class
class messageFun():
    def __init__(self, message):
        self.message = message


    async def dadJoke(self):
        url = "https://icanhazdadjoke.com/slack"
        response = requests.get(url)
        value = response.json()["attachments"][0]["text"]
        await client.send_message(self.message.channel, value)


    async def lvlCheck(self, sLvl: int):
        tempSpell = ""
        for i in range(318):
            spell = spellsList[i]
            if len(tempSpell) > 1950:
                overflow = self.overFlow(i, sLvl, "level")
                await client.send_message(self.message.channel, overflow)
                tempSpell = ""
            elif spell["level"] == sLvl:
                tempSpell = tempSpell + spell["name"] + "\n"
        await client.send_message(self.message.channel, tempSpell)

    # class organization
    async def classCheck(self, sClass: str):
        tempSpell = ""
        for i in range(318):
            spell = spellsList[i]
            for j in range(len(spell["classes"])):
                if len(tempSpell) > 1950:
                    overflow = self.overFlow(i, sClass, "classes")
                    await client.send_message(self.message.channel, overflow)
                    tempSpell = ""
                if spell["classes"][j]["name"] == sClass.capitalize():
                    tempSpell = tempSpell + spell["name"] + "\n"
        await client.send_message(self.message.channel, tempSpell)

    # class overflow
    def overFlow(self, num, sClass, type):
        tempsSpell = ""
        for i in range(318 - num):
            spell = spellsList[i]
            for j in range(len(spell[type])):
                if len(tempsSpell) > 1950:
                    return "Error: overFlow = full"
                if type == "classes":
                    if spell[type][j]["name"] == sClass.capitalize():
                        tempsSpell = tempsSpell + spell["name"] + "\n"
                else:
                    if spell[type] == sClass.capitalize():
                        tempsSpell = tempsSpell + spell["name"] + "\n"
        return tempsSpell


    # spell def
    async def spellAll(self):
        if self.message.content.startswith("|"):
            for i in range(318):
                spell = spellsList[i]
                total = ""

                # print(spell)
                # print(message.content[1:])

                if self.message.content[1:].title().startswith(spell["name"]):
                    total = total + "Name: "+ spell["name"] + "\n"

                    if spell["level"] == 0:
                        total = total + "Level: Cantrip" + "\n"
                    else:
                        total = total + "Level: " + str(spell["level"]) + "\n"

                    total = total + "Range: "+ spell["range"] + "\n"
                    total = total + "Duration: "+ spell["duration"] + "\n"

                    if spell["ritual"] == "yes":
                        total = total + "Ritual: " + spell["ritual"] + "\n"
                    if spell["concentration"] == "yes":
                        total = total + "Concentration: " + spell["concentration"] + "\n"

                    total = total + "School:" + "\n"
                    total = total + "~" + spell["school"]["name"] + "\n"
                    # for j in range(len(spell["school"])):
                    #     await client.send_message(self.message.channel, "~" + spell["school"][j]["name"])

                    total = total + "Classes:" + "\n"
                    for j in range(len(spell["classes"])):
                        total = total + "~" + spell["classes"][j]["name"] + "\n"

                    total = total + "Description:" + "\n"
                    for j in range(len(spell["desc"])):
                        total = total + "~" + spell["desc"][j] + "\n"

                    await client.send_message(self.message.channel, total)

                # if self.message.content[1:].title().startswith(spell["name"]):
                #     await client.send_message(self.message.channel, "Name: "+ spell["name"])
                #
                #     if spell["level"] == 0:
                #         await client.send_message(self.message.channel, "Level: Cantrip")
                #     else:
                #         await client.send_message(self.message.channel, "Level: " + spell["level"])
                #
                #     await client.send_message(self.message.channel, "Range: "+ spell["range"])
                #     await client.send_message(self.message.channel, "Duration: "+ spell["duration"])
                #
                #     if spell["ritual"] == "yes":
                #         await client.send_message(self.message.channel, "Ritual: " + spell["ritual"])
                #     if spell["concentration"] == "yes":
                #         await client.send_message(self.message.channel, "Concentration: " + spell["concentration"])
                #
                #     await client.send_message(self.message.channel, "School:")
                #     await client.send_message(self.message.channel, "~" + spell["school"]["name"])
                #     # for j in range(len(spell["school"])):
                #     #     await client.send_message(self.message.channel, "~" + spell["school"][j]["name"])
                #
                #     await client.send_message(self.message.channel, "Classes:")
                #     for j in range(len(spell["classes"])):
                #         await client.send_message(self.message.channel, "~" + spell["classes"][j]["name"])
                #
                #     await client.send_message(self.message.channel, "Description")
                #     for j in range(len(spell["desc"])):
                #         await client.send_message(self.message.channel, "~" + spell["desc"][j])



@client.event
async def on_message(message):
    extra = messageFun(message)

    print(message.author)
    print(message.content)

    # await client.send_message()

    # bot replying to self stops
    if message.author == client.user:
        return

    # print(message.author)
    # if message.author == message.author:
    #     await client.send_message(message.channel, message.content)

    #Hello
    if message.content.startswith('|hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    #Beese Churger
    elif message.content.startswith('beese churger'):
        await client.delete_message(message)
        await client.send_message(message.channel, "Welcome to Mcdownald's \n Do you want a phucking \n Beese Churger?")

    # if message.content.startswith('|clear'):
    #     await extra.clear()

    # if message.content.startswith('|clear'):
    #     print(client.logs_from(message.channel))
    #     # mgs = []  # Empty list to put all the messages in the log
    #     # # number = int(10)  # Converting the amount of messages to delete to an integer
    #     # async for x in client.logs_from(message.message.channel):
    #     #     mgs.append(x)
    #     if client.logs_from(message.message.channel) == "<coroutine object messageFun.spellOverFlow at 0x000001C72B822AF0>":
    #         print("rar")

    if message.content.startswith("|lvl 0") or message.content.startswith("|lvl cantrip"):
        await extra.lvlCheck(0)
    elif message.content.startswith("|lvl 1"):
        await extra.lvlCheck(1)
    elif message.content.startswith("|lvl 2"):
        await extra.lvlCheck(2)
    elif message.content.startswith("|lvl 3"):
        await extra.lvlCheck(3)
    elif message.content.startswith("|lvl 4"):
        await extra.lvlCheck(4)
    elif message.content.startswith("|lvl 5"):
        await extra.lvlCheck(5)
    elif message.content.startswith("|lvl 6"):
        await extra.lvlCheck(6)
    elif message.content.startswith("|lvl 7"):
        await extra.lvlCheck(7)
    elif message.content.startswith("|lvl 8"):
        await extra.lvlCheck(8)
    elif message.content.startswith("|lvl 9"):
        await extra.lvlCheck(9)

    # classes
    if message.content.startswith("|sorcerer") or message.content.startswith("|Sorcerer"):
        await extra.classCheck("sorcerer")
    elif message.content.startswith("|wizard") or message.content.startswith("|Wizard"):
        await extra.classCheck("wizard")
    elif message.content.startswith("|bard") or message.content.startswith("|Bard"):
        await extra.classCheck("bard")
    elif message.content.startswith("|cleric") or message.content.startswith("|Cleric"):
        await extra.classCheck("cleric")
    elif message.content.startswith("|paladin") or message.content.startswith("|Paladin"):
        await extra.classCheck("paladin")
    elif message.content.startswith("|druid") or message.content.startswith("|Druid"):
        await extra.classCheck("druid")
    elif message.content.startswith("|warlock") or message.content.startswith("|Warlock"):
        await extra.classCheck("warlock")
    elif message.content.startswith("|ranger") or message.content.startswith("|Ranger"):
        await extra.classCheck("ranger")


    if message.content.startswith("|wild magic list"):
        for j in range(5):
            listM = ""
            j = j * 10
            for i in range(10):
                i = i + j
                listM = listM + possibleResponse[i] + "\n \n"
                print(listM)
            await client.send_message(message.channel, listM)

    elif message.content.startswith("|wild magic"):
        await client.send_message(message.channel, random.choice(possibleResponse))

    if message.content.startswith("|joke"):
        await extra.dadJoke()

    await extra.spellAll()

    if message.content.startswith("|fuck"):
        await client.send_message(message.channel, "Fuck You")


    await client.process_commands(message)


@client.command(pass_context= True)
async def help(ctx):
    embed = discord.Embed(
        color = discord.Colour.orange()
    )

    embed.set_author(name="Help")
    embed.add_field(name="|helpSpell", value="~Helps search spells", inline= False)
    embed.add_field(name="|[spell name]", value="~Gives all the information on that spell", inline=False)
    embed.add_field(name="|wild magic", value="~Displays a random wild magic spell", inline=False)
    embed.add_field(name="|joke", value="~Sends some internet made dad jokes", inline=False)
    embed.add_field(name="|helpAdv", value="~Advance list of commands", inline=False)

    await client.send_message(ctx.message.channel, embed= embed)

@client.command(pass_context= True)
async def helpAdv(ctx):
    embed = discord.Embed(
        color = discord.Colour.orange()
    )

    embed.set_author(name="Help")
    embed.add_field(name="|[class]", value="~Gives all spells for that class", inline= False)
    embed.add_field(name="|lvl [level]", value="~Gives all spells for that level", inline=False)
    embed.add_field(name="|[spell name]", value="~Gives all the information on that spell", inline=False)
    embed.add_field(name="|wild magic list", value="~Displays all wild magic spells", inline=False)

    await client.send_message(ctx.message.channel, embed= embed)

@client.command(pass_context= True)
async def helpSpell(ctx):
    embed = discord.Embed(
        color = discord.Colour.orange()
    )

    embed.set_author(name="Help")
    embed.add_field(name="|classes", value="~Gives a list of avaliable class", inline= False)
    embed.add_field(name="|lvl [level]", value="~Gives all spells in that level from cantrip-9", inline=False)

    await client.send_message(ctx.message.channel, embed= embed)

@client.command(pass_context= True)
async def classes(ctx):
    embed = discord.Embed(
        color = discord.Colour.orange()
    )

    embed.set_author(name="Class")
    embed.add_field(name="|Sorcerer", value="|Wizard", inline= False)
    embed.add_field(name="|Bard", value="|Cleric", inline=False)
    embed.add_field(name="|Warlock", value="|Paladin", inline=False)
    embed.add_field(name="|Druid", value="|Ranger", inline=False)

    await client.send_message(ctx.message.channel, embed= embed)

client.run(token)
