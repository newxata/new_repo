# Excesize 1

from datetime import datetime

# Створення функції
def get_days_from_today(date):
    # Запускаємо оператор try для винятку
    try:
        # Претворюємо параметр date у обʼєкт datetime
        date = datetime.strptime(date,'%Y-%m-%d')
        # Отримаємо поточну дату
        current_date = datetime.today()
        # Розраховуємо різницю між поточною датою та заданою датою як ціле число
        diff_date = current_date.toordinal() - date.toordinal()
        # Повертаємо наш розрахунок
        return diff_date
    # Додаємо виняток на випадок введення заданої дати у неправильному форматі
    except ValueError:
        return f'{date} invalid date format. Please enter the date in the correct format: YYYY-MM-DD'

print('Excesize 1:')
print(get_days_from_today("2024-10-01"))

print('-' * 50)



# Excesize 2

import random

def get_numbers_ticket(min_value, max_value, quantity):
    # Задаємо обмеження функції
    if min_value < 1 or max_value > 1000 or quantity > (max_value - min_value + 1):
        return []

    # Генеруємо вказану кількість випадкових, унікальних чисел в заданому діапазоні і сортуємо список
    numbers = sorted(random.sample(range(min_value, max_value + 1), quantity))
    return numbers

# Перевірка на коректність введення даних
try:
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print('Excesize 2:')
    print('Your lottery numbers: ', lottery_numbers)
except NameError:
    print('Всі значення мають бути введені числом')


"""
Доопрацював функцію. Якщо параметри не відповідають заданим обмеженням, 
то функція повертає не пустий список, а повідомлення з помилкою. 
"""
# import random
#
# def get_numbers_ticket(min_value, max_value, quantity):
#
#     if min_value < 1:
#         return f'Мінімальне значення не може бути менше 1'
#     elif max_value > 1000:
#         return f'Максимальне значення не може бути більше 1000 '
#     elif quantity > (max_value - min_value + 1):
#         return f'Кількість випадкових варіантів чисел перевищує доступний діапазон'
#     elif quantity == 0:
#         return f'Кількість випадкових варіантів чисел не може дорівнювати нулю'
#     numbers = sorted(random.sample(range(min_value, max_value + 1), quantity))
#     return numbers
# try:
#     lottery_numbers = get_numbers_ticket(min_value=int(input('Enter min value: ')), max_value=int(input('Enter max value: ')), quantity=int(input('Enter quantity: ')))
#     print('Your lottery numbers: ', lottery_numbers)
# except ValueError:
#     print('Всі значення мають бути введені числом')