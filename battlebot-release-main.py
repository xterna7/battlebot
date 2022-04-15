# 키배봇 by xterna7
import re
import random
from ast import literal_eval

import discord
from discord.ext import commands
import colorama
from colorama import Fore

client = commands.Bot(command_prefix = "/", self_bot = True, help_command = None) 
token= ""#your token
READY = "키배봇 is running!"

#학습가능 : /mod1
file = open('config/replist.ini',mode='r', encoding='UTF8')
allrp = file.read()
replist = literal_eval(allrp)#dict

#학습가능 : /mod2
file2 = open('config/badwordlist.ini',mode='r', encoding='UTF8')
allbdwd = file2.read()
ylist = literal_eval(allbdwd)#list

#학습가능 : /mod3
file3 = open('config/randomword.ini',mode='r', encoding='UTF8')
allrwd = file3.read()
randy = literal_eval(allrwd)#list


class Lrn:
    def __init__(self):
        self.status = 0
        
    def learn(text, key):
        value = replist.get(key)
        if value == None:
            replist[key] = []
            file = open('config/replist.ini',mode='w', encoding='UTF8')
            file.write(str(replist))
            file.close()
            print('key가 존재하지 않아 생성만 했습니다. 다시 해주세요')
        else:
            replist[key].append(text)
            file = open('config/replist.ini',mode='w', encoding='UTF8')
            file.write(str(replist))
            file.close()
            print('학습 완료')

    def learn2(text):
        ylist.append(text)
        file = open('config/badwordlist.ini',mode='w', encoding='UTF8')
        file.write(str(ylist))
        file.close()
        print('학습 완료. 상대가 이 단어를 쳤을 때 반박합니다..')

    def learn3(text):
        randy.append(text)
        file = open('config/badwordlist.ini',mode='w', encoding='UTF8')
        file.write(str(randy))
        file.close()
        print('학습 완료')
    
class Rmv:
    def __init__(self):
        self.plain = None

    def remove1(self, key):
        replist[key].remove(self.plain)
        file = open('config/replist.ini',mode='w', encoding='UTF8')
        file.write(str(replist))
        file.close()
        print('제거 완료')
        
    def remove1key(self, key):
        del replist[key]
        file = open('config/replist.ini',mode='w', encoding='UTF8')
        file.write(str(replist))
        file.close()
        print('제거 완료')

    def remove2(self, value):
        ylist.remove(value)
        file = open('config/badwordlist.ini',mode='w', encoding='UTF8')
        file.write(str(ylist))
        file.close()
        print('제거 완료')

    def remove3(self, value):
        randy.remove(value)
        file = open('config/randomword.ini',mode='w', encoding='UTF8')
        file.write(str(allrwd))
        file.close()
        print('제거 완료')

lrn = Lrn()
rmv = Rmv()

string=None
new_string=None 
plain=None
status=None
SE=None
keylist=None
tet = None

masterlist = []

help_explain = '''
```
mod1:메인욕 학습 시스템(with key)
mod2:상대방이 mod2 명령어로 학습시킨 말을 할 시에 답장함
mod3:랜덤욕 학습 시스템
rm-mod1:메인욕 제거 시스템(with key)
rm-mod2:mod2로 학습시킨것을 제거하는 시스템
rm-mod3:랜덤욕 제거 시스템

made by xterna7
```
'''
def checky1(t):
    if t in ylist:
        return True
    else:
        return 

def checky2(t):
    for i in range(len(ylist)):
        if t.find(ylist[i]) != -1:
            return True


@client.event
async def on_ready():
    print(READY)
    await client.change_presence(status=discord.Status.online, activity=discord.Game("BATTLEBOT V1"))

@client.command()
async def help(ctx): 
    await ctx.message.delete() 
    await ctx.send("Hello example") 

@client.event
async def on_message(message):
    global string, new_string, plain, status, SE, keylist
    await client.process_commands(message)

    id = message.author.id

    masterlist.append(842010766927593512)#hyperdemented

    if message.author.id == client.user.id:
        return

    string = message.content
    new_string = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣a-zA-Z]","",string)

    plain = new_string

    status = -1
    SE = 0
    keylist = []

    if message.content == '.help':
        await message.channel.send(help_explain)

    if message.content.startswith('.mod1;') and id in masterlist:
        try:
            tolrn = string.split(';')[1]
            key = string.split(';')[2]
            Lrn.learn(tolrn, key)
            await message.channel.send('학습 완료')
        except:
            await message.channel.send('오류 발생. Usage: .mod1;[배울내용];[key값]')

    if message.content.startswith('.mod2;') and id in masterlist:
        try:
            tolrn = string.split(';')[1]
            Lrn.learn2(tolrn)
            await message.channel.send('학습 완료')
        except:
            await message.channel.send('오류 발생. Usage: .mod2;[배울내용]')

    if message.content.startswith('.mod3;') and id in masterlist:
        try:
            tolrn = string.split(';')[1]
            Lrn.learn3(tolrn)
            await message.channel.send('학습 완료')
        except:
            await message.channel.send('오류 발생. Usage: .mod3;[배울내용]')

    if message.content.startswith('.rm-mod1;') and id in masterlist:
        try:
            torm = string.split(';')[1]
            key = string.split(';')[2]
            rmv.plain = torm
            rmv.remove1(key)
            SE -= 1
            await message.channel.send('제거 완료')
        except:
            await message.channel.send('오류 발생. Usage: .rm-mod1;[지울내용];[key값]')

    if message.content.startswith('.rmk-mod1;') and id in masterlist:
        try:
            key = string.split(';')[1]
            rmv.remove1key(key)
            keylist.remove(key)
            SE -= len(replist[key])
            await message.channel.send('제거 완료')
        except:
            await message.channel.send('오류 발생. Usage: .rmk-mod1;[지울key값]')

    if message.content.startswith('.rm-mod2;') and id in masterlist:
        try:
            value = string.split(';')[1]
            rmv.remove2(value)
            await message.channel.send('제거 완료')
        except:
            await message.channel.send('오류 발생. Usage: .rm-mod2;[지울내용]')

    if message.content.startswith('.rm-mod3;') and id  in masterlist:
        try:
            value = string.split(';')[1]
            rmv.remove3(value)
            await message.channel.send('제거 완료')
        except:
            await message.channel.send('오류 발생. Usage: .rm-mod3;[지울내용]')

    for i in replist.keys():
        SE += len(replist[i])
        keylist.append(i)

    def replyabout():
        global string, new_string, plain, status, SE, keylist,tet
        if status == 1:
            how = random.randint(1,3)
            #print(how)
            if how == 1:
                if SE == 0:
                    rindex = random.randrange(len(randy))
                    tet = randy[rindex]
                else:
                    value = replist.get('일반대응')
                    if not value == None:
                        if not replist['일반대응'] == []:
                            rindex = random.randrange(len(replist['일반대응']))

                            tet = replist['일반대응'][rindex]

                            del replist['일반대응'][rindex]
                            SE -= 1
                            
                        else:
                            rindex = random.randrange(len(randy))
                            tet = randy[rindex]
                    else:
                        rindex = random.randrange(len(randy))
                        tet = randy[rindex]
            elif how == 2:
                if SE == 0:
                    rindex = random.randrange(len(randy))
                    tet = randy[rindex]
                else:
                    value2 = replist.get('법적대응')
                    if not value2 == None:
                        if not replist['법적대응'] == []:
                            rindex = random.randrange(len(replist['법적대응']))
   
                            tet = replist['법적대응'][rindex]

                            del replist['법적대응'][rindex]
                            SE -= 1
                        else:
                            rindex = random.randrange(len(randy))
                            tet = randy[rindex]
                    else:
                        rindex = random.randrange(len(randy))
                        tet = randy[rindex]
            elif how == 3:
                if SE == 0:
                    rindex = random.randrange(len(randy))
                    tet = randy[rindex]
                else:
                    rkey = random.choice(keylist)
                    if not replist[rkey] == []:
                        rindex = random.randrange(len(replist[rkey]))

                        tet = replist[rkey][rindex]

                        del replist[rkey][rindex]
                        SE -= 1
                    else:
                        rindex = random.randrange(len(randy))
                        tet = randy[rindex]
        elif status == -1:
            return

    if checky1(new_string):
        status = 1
        replyabout()
        await message.channel.send(tet)

    elif checky2(new_string):
        status = 1
        replyabout()
        await message.channel.send(tet)

client.run(token, bot = False)

