import random # импортируем модуль генерации случайных чисел

def random_matrix(m, n, min_value=0, max_value=100):
    """
    Создаем функцию, которая будет генерировать матрицу случайных числе
    по значениям M и N с помощью рандомного списка
    """
    return [[random.randint(min_value, max_value) for _ in range(n)] for _ in range(m)]

# Создаем элементы где m - количсетво списков, а n - количество числе в списке
matrix = random_matrix(4, 20)
for row in matrix:
    print(row)
