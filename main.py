import vk
import requests

def parseSubGroups(lesson, audience):
    import re
    lesson.strip()
    numbers = re.sub("[^-?0-9]+", ' ', lesson)
    search = numbers.strip().split(' ')
    rooms = audience.strip().split(' ')

    if len(rooms) == len(search):
        result = ""
        i = 1
        while i < len(search):
            result += lesson.split(search[i])[0] + " || кабинет: " + \
                      rooms[i - 1] + "\n"
            lesson = lesson[lesson.index(search[i]):]
            i += 1
        result += lesson + " || кабинет: " + \
                  rooms[len(rooms) - 1] + "\n"
        return result
    else:
        return lesson + " || кабинет(кабинеты): " + rooms

if __name__ == '__main__':
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
                        s = s + 'Номер пары: ' + str(k['number']) + '\n'
                        s += parseSubGroups(k['lesson'], k['audience'])
                        s = s + '                                                  \n'

                    break
            break

    vkapi.messages.send(message=s, user_id=vkid)
