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