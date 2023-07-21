import discord
import asyncio
import FinanceDataReader as fdr

intents = discord.Intents.all()
client = discord.Client(intents=intents)

def check(code):
    try:
        df = fdr.DataReader(code)
        return True
    except:
        return False

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
        chart = message.content.split(" ")[2]
        date = message.content.split(" ")[3]
        if check(stockCode):
            if chart == "선차트"
                areaChart = {"1일": "day", "1주일": "week", "3개월": "month3", "1년": "year", "3년": "year3", "5년": "year5", "10년": "year10"}
                try:
                    embed = discord.Embed(title="[ 검색 ]", description="종목을 조회했습니다!", color=0xfead67)
                    embed.set_image(url=f"https://ssl.pstatic.net/imgfinance/chart/item/area/{areaChart[date]}/{stockCode}.png")
                    await message.channel.send(embed=embed)
                except:
                    embed = discord.Embed(title="[ 검색 ]", description="잘못된 차트 종류입니다! 차트의 종류는 `1일`, `1주일`, `3개월`, `1년`, `3년`, `5년`, `10년`중 하나여야 합니다!", color=0xfead67)
                    await message.channel.send(embed=embed)
            elif chart == "봉차트":
                candleChart = {"일봉": "day", "주봉": "week", "월봉": "month"}
                try:
                    embed = discord.Embed(title="[ 검색 ]", description="종목을 조회했습니다!", color=0xfead67)
                    embed.set_image(url=f"https://ssl.pstatic.net/imgfinance/chart/item/candle/{candleChart[date]}/{stockCode}.png")
                    await message.channel.send(embed=embed)
                except:
                    embed = discord.Embed(title="[ 검색 ]", description="잘못된 차트 종류입니다! 차트의 종류는 `일봉`, `주봉`, `월봉`중 하나여야 합니다!", color=0xfead67)
                    await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(title="[ 검색 ]", description="잘못된 차트 종류입니다! 차트의 종류는 `선차트`, `봉차트`중 하나여야 합니다!", color=0xfead67)
                await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="[ 검색 ]", description="잘못된 종목 코드입니다!", color=0xfead67)
            await message.channel.send(embed=embed)

client.run("token")