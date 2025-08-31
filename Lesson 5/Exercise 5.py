import tabulate #Скачиваем библиотеку для создания таблицы

def summa_list(numbers):
    '''
    Пишем функцию для анализа списка и определения суммы, максимального и минимального
    значения чисел из списка
    return - завершает выполнение функции и возвращает управление вызывающей функции
    '''

    sum_of_numbers = sum(numbers)
    min_number = min(numbers)
    max_number = max(numbers)
    return sum_of_numbers, min_number, max_number

# Наш список чисел
numbers_1 = [10, 15, 43, 96, 85]

# Передаем значения списка numbers_1 в функцию summa_list
sum_result, min_result, max_result = summa_list(numbers_1)

# Выводим результат в таблицу
data = [
    ["Сумма всех чисел", "Минимальное значени числа", "Максимальное значние числа"],
    [sum_result, min_result, max_result]
]
results = tabulate.tabulate(data)
print(results)