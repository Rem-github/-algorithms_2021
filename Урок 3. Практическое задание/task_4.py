"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib

def url_check(user_url):
    res = hashlib.sha256(user_url.encode() + salt.encode()).hexdigest()
    if res in user_cache.values():
        print('URL уже есть в кэше')
    else:
        user_cache[user_url] = res
        print(f'URL {user_url} добавлен в кэш')

user_cache = {}
salt = 'salt'

url_check('www.yandex.ru')
url_check('www.yandex.ru')
url_check('www.mail.ru')
print(user_cache)
