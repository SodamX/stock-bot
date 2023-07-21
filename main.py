import discord
import asyncio
import requests

intents = discord.Intents.all()
client = discord.Client(intents=intents)

def check(code):
    d6 = today.strftime("%Y%m%d")
    url = "https://api.finance.naver.com/siseJson.naver?symbol=005930&requestType=1&startTime=20140817&endTime=20210605&timeframe=week"
    res = requests.get(url).json()

@client.event
async def on_ready():
  async def message(games):
    await client.wait_until_ready()
    while not client.is_closed():
        for game in games:
            await client.change_presence(status = discord.Status.idle, activity = discord.Game(game))
            await asyncio.sleep(10)
  await message(["stock-bot", "실제 있는 주식 정보를 받아오는 봇입니다!"])

@client.event
async def on_message(message):
    if message.content.startswith("!검색"):
        stockCode = message.content.split(" ")[1]
        if stockCode.isdigit():
            embed = discord.Embed(title="[ 검색 ]", description="멘탈 복구 성공!", color=0xfead67)
            embed.set_image(url=f"")
            await message.channel.send(embed=embed)

client.run("token")