import random
import string

def generate_registration_data():
    name_lenght = random.randint(5, 7)
    name = ''.join(random.choices(string.ascii_lowercase, k=name_lenght) + random.choices(string.digits, k=3))

    email_length = random.randint(5, 7)
    email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=email_length)) + '@yandex.ru'
    
    password_length = random.randint(6, 8)
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=password_length))
    return name, email, password  # Возвращаем  (name, email, password)
