import random

# Создаём случайную матрицу 3x4
matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(3)]

# Показываем матрицу
print("Сгенерированная матрица:")
for row in matrix:
    print(row)

# Пользователь вводит число для поиска
H = int(input("\nВведите число для поиска (H): "))

# Проверяем столбцы
with_H = [j for j in range(4) if any(row[j] == H for row in matrix)]
without_H = [j for j in range(4) if j not in with_H]

# Выводим результат
print(f"\nСтолбцы с числом {H}: {[x+1 for x in with_H]}")  # Добавляем +1 к индексу
print(f"Столбцы без числа {H}: {[x+1 for x in without_H]}")