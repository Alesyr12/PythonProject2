import time

def measure_time(func):
    def wrapper():
        start = time.time()          # Фиксируем начало
        func()                       # Видимость работы
        end = time.time()            # Фиксируем окончание
        print(f"Время выполнения: {end - start:.2f} сек") # Выводим результат засеченного времени
    return wrapper


@measure_time
def my_function():
    print("Функция начала обработку....")
    time.sleep(3) # Делаем исскуственную задержку в 3 сек
    print("Функция завершила работу")

# Вызываем функцию
my_function()