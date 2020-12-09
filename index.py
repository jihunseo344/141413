#기본 모듈
import discord
import openpyxl

#클라이언트는 디스코드 클라이언트
client = discord.Client()

#만약 봇이 준비가 되면
async def on_ready():
    #'ready' 를 프린트 한다.
    print('BOT LOGIN')

@client.event
async def on_message(message):
    if message.content.startswith('$배워'):
        file = openpyxl.load_workbook('log.xlsx')
        work = message.content.split(' ')
        sheet = file.active
        for i in range(1,51):
            if sheet['A' + str(i)].value =='-' or sheet['A'+str(i)].value == work[1]:
                sheet['A' + str(i)].value = work[1]
                sheet['B' + str(i)].value = work[2]
                sheet['C' + str(i)].value = message.author.name
                embed = discord.Embed(colour=discord.Colour(0xFFFFFF))
                embed.set_author(name=f'이제 {work[1]} 이라고 말하면 {work[2]} 라고 말할게용:)!')
                await message.channel.send(embed=embed)
                break
        file.save('log.xlsx')

    if message.content.startswith(''):
        file = openpyxl.load_workbook('log.xlsx')
        work = message.content
        sheet = file.active
        for i in range(1,51):
            if sheet['A'+str(i)].value == work:
                await message.channel.send(sheet['B' + str(i)].value + "\n" + sheet["C" + str(i)].value + "님이 알려 주셨어용 !")
                break

    
#구동 할 봇 토큰
client.run("Nzg0MjM4MjU2MTM2MTI2NDc1.X8mYyg.RnXy0J_hD3S72gWRL6cdwZ4c5Jw")
