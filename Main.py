import vk

# access_token
key = ''
session = vk.Session(access_token=key)  # Создание сессии
vkapi = vk.API(session, timeout=10, v='5.58')

messages = vkapi.messages.get(out=0, count=5)
for p in messages['items']:
    print(p['body'])