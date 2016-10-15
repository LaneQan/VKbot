import vk
import requests


# Токен
key = ''
with open('key.config', 'r') as myfile:
    key = myfile.read().replace('\n', '')

# Создание сессии
session = vk.Session(access_token=key)
vkapi = vk.API(session, timeout=10, v='5.58')

def firstgroup(str):
    return str[0:str.index('2')]
def secondgroup(str):
    if '3' not in str:
        return str[str.index('2'):len(str)]
    else:
        return str[str.index('2'):str.index('3')]

def thirdgroup(str):
    return str[str.index('3'):len(str)]

def thirdcab(s):
    return s[s.rindex(' ') + 1:len(s)]

def secondcab(s):
    if s.count(' ') == 2:
        return s[s.index(' ')+1:s.rindex(' ')]
    elif s.count(' ') == 1:
        return s[s.index(' '):len(s)]

def firstcab(s):
    return s[0:s.index(' ')]




# API
r = requests.get('http://s1.al3xable.me/method/getStudent')
lessons = r.json()

vkid = ''



messages = vkapi.messages.get(out=0, count=10)
s = '                                                  \n'
for p in messages['items']:
    if 'Расписание' in p['body']:
        vkid = p['user_id']
        group = p['body']
        group = group.replace(' ', '')
        group = group.replace('Расписание', '')
        for index, d in enumerate(lessons['data']['groups']):
            if d['title'] == group:
                for k in lessons['data']['groups'][index]['lessons']:
                    if '3' in k['lesson']:
                        s = s + 'Номер пары: ' + str(k['number']) + '\n'
                        s = s + (firstgroup(k['lesson']) + ' || кабинет: ' + firstcab(k['audience']) + '\n')
                        s = s + (secondgroup(k['lesson']) + ' || кабинет: ' + secondcab(k['audience']) + '\n')
                        s = s + (thirdgroup(k['lesson']) + ' || кабинет: ' + thirdcab(k['audience']) + '\n')
                        s = s + '                                                  \n'
                    elif '2' in k['lesson']:
                        s = s + 'Номер пары: ' + str(k['number']) + '\n'
                        if '1' in k['lesson']:
                            s = s + (firstgroup(k['lesson']) + ' || кабинет: ' + firstcab(k['audience']) + '\n')
                        s = s + (secondgroup(k['lesson']) + ' || кабинет: ' + secondcab(k['audience']) + '\n')
                        s = s + '                                                  \n'
                    else:
                         s = s + 'Номер пары: ' + str(k['number']) + '\n'
                         s = s + (k['lesson'] + ' || кабинет: ' + k['audience'] + '\n')
                         s = s + '                                                  \n'
                break
        break
vkapi.messages.send(message=s, user_id=vkid)


#print(lessons['title'][0]['lesson'])