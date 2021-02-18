import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("개발")
    await client.change_presence(status=discord.Status.online, activity=game)




@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("ㅎㅇ")
    if message.content.startswith("나 간다"):
        await message.channel.send("ㅃㅇ")
    if message.content.startswith("테스트"):
        await message.channel.send("정상작동중")
    if message.content.startswith("박승재"):
        await message.channel.send("다람쥐")

    if message.content.startswith("/사진"):
        pic = message.content.split(" ") [1]
        await message.channel.send(file=discord.File(pic))











client.run("ODExNDc0OTI5NDEyNzM1MDM4.YCyu6w.2jkvKIp96kmsYpcnaEUa4biJap4")





