'''
Создаем функцию, которая будет проверять делится ли число на 1
и само на себя
'''
def is_prime(n):
    if n < 2:
        return False
    # Проверяем нечётные делители от 2 до квадратного корня из n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Введите число: "))
print(f"{num} — {'простое' if is_prime(num) else 'составное'} число.")