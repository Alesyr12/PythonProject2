import random

# Созадем функцию, которая буде генерировать случайную матрицы
def generate_random_matrix(rows, cols):
    """ a и b - представляют числа, из которыз будет сгенерирована матрица"""
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

def add_even_ones_column(matrix):
    """Добавляет столбец с количеством чётных единиц в строке."""
    new_column = []
    for row in matrix:
        count_ones = sum(row)  # Подсчитываем кол-во 1 в строке

        # # Кол-во 1 > 0 - добавляем значние, < 0 - ставим 0
        new_column.append(count_ones if count_ones % 2 == 0 else 0)

    # Теперь добавляем столбец
    for i, row in enumerate(matrix):
        row.append(new_column[i])
    return matrix

def print_matrix(matrix):
    """Выводит матрицу в читаемом виде."""
    for row in matrix:
        print(row)


M = 4  # Количество строк
N = 5  # Количество столбцов (до добавления нового)


random_matrix = generate_random_matrix(M, N)
print("Исходная матрица:")
print_matrix(random_matrix)


new_matrix = add_even_ones_column(random_matrix)
print("\nМатрица с добавленным столбцом:")
print_matrix(new_matrix)