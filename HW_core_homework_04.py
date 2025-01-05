# Excesize 1

def total_salary(path):
    try:
        total = 0
        count = 0

        # Читаємо файл з данними у відповідному кодуванні
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Приводимо рядки до структури - "імʼя,зарплата"
                    name, salary = line.strip().split(',')
                    total += int(salary) # Додаємо значення до змінної total
                    count += 1 # Рахуємо кількість оброблених рядків
                # Виключення коли рядок не відповідає структурі - "імʼя,зарплата"    
                except ValueError:
                    print(f'Рядок не відповідає формату: {line.strip()}')
        # На випадок коли всі значення дорівнюють нулю
        if count == 0:
            return 0, 0
        # Розрахунок середньої зарплати
        average = total / count
        return total, average
    # Виключення коли файл за зазначеною адресою не знайдено 
    except FileNotFoundError:
        print(f'Файл не знайдено!')
        return 0, 0

total, average = total_salary('path/to/salary_file.txt')
print(f'Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}')



# Excesize 2

def get_cats_info(path):
    # Створюємо пустий список котів
    cats_list = []
    try:
        # Читаємо файл з данними у відповідному кодуванні
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо прочитанні значення за комами
                id, name, age = line.strip().split(',')
                # Присвоюємо отриманні значення відповідному ключу списку
                cats_list.append({
                    'id': id,
                    'name': name,
                    'age': age
                })
        # Повертаємо список
        return cats_list
    # Додаємо відповідні виключення 
    except ValueError:
        return f'Рядок не відповідає формату: {line.strip()}'
    except FileNotFoundError:
        return f'Файл не знайдено!'

    

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)



# Excesize 4

# Функція яка приймає рядок вводу користувача
def parse_input(user_input):
    # Повертаємо перше слово як команду та зберігаємо у змінній cmd, решту зберігаємо як список аргументів *args
    cmd, *args = user_input.split()
    # Видаляємо зайві пробіли та перетворюємо на нижній регістр
    cmd = cmd.strip().lower()
    return cmd, *args

# Функція додавання нового контакту до словника контактів
def add_contact(args, contacts):
    # Обмеження на введення більше значень ніж name та phone
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return 'Contact added.'
    else:
        return 'Error. Enter name and phone.'

# Функція зміни номеру телефону для контакту який вже існує в списку
def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        # Умова якщо імʼя відсутнє в списку
        if name in contacts:
            contacts[name] = phone
            return 'Contact updated.'
        else:
            return 'No contact.'
    else:
        return 'Error. Enter name and phone.'

# Функція виведення номеру телефону
def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return 'No contact.'
    else:
        return 'Error. Enter name.'

# Функція виведення усіх збережених контактів
def show_all(contacts):
    return contacts

def main():
    # Створюємо словник контактів
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        # Змінна command отримує перше введене слово та стає командою, а змінна *args списком з усіх інших значень
        command, *args = parse_input(user_input)

        # Якщо команда close або exit то зупиняємо цикл
        if command in ['close', 'exit']:
            print('Good bye!')
            break

        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print('Invalid command.')

if __name__ == '__main__':
    main()