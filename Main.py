import vk
import requests


# Токен
key = ''
with open('key.config', 'r') as myfile:
    key = myfile.read().replace('\n', '')

# Создание сессии
session = vk.Session(access_token=key)
vkapi = vk.API(session, timeout=10, v='5.58')



# API
r = requests.get('http://s1.al3xable.me/method/getStudent')
lessons = r.json()

vkid = 276887954


messages = vkapi.messages.get(out=0, count=10)
s = ''
for p in messages['items']:
    if 'Расписание' in p['body']:
        group = p['body']
        group = group.replace(' ', '')
        group = group.replace('Расписание', '')
        for index, d in enumerate(lessons['data']['groups']):
            if d['title'] == group:
                for k in lessons['data']['groups'][index]['lessons']:
                    s = s + (k['lesson'] + 'в кабинете(ах) ' + k['audience'] + '\n')
                break
        break
vkapi.messages.send(message=s, user_id=vkid)


#print(lessons['title'][0]['lesson'])