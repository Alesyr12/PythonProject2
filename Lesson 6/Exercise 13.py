import tabulate

def diagonal_sums(matrix):

    # Если матрица пуста
    if not matrix:
        # Если матрица пустая, выводим нули
        return 0, 0

    # Высчитываем сумму диогонали
    main_sum = 0
    # Высчитываем сумму второй диагонали
    secondary_sum = 0


    rows = len(matrix)
    cols = len(matrix[0])

    # Главная диагональ: matrix[0][0], matrix[1][1], matrix[2][2], ...
    for i in range(min(rows, cols)):  # Идём до меньшего из rows и cols
        main_sum += matrix[i][i]

    # Побочная диагональ: matrix[0][последний], matrix[1][предпоследний], ...
    for i in range(min(rows, cols)):
        j = cols - 1 - i  # Вычисляем индекс столбца для побочной диагонали
        secondary_sum += matrix[i][j]

    return main_sum, secondary_sum

matrix = [
    [1, 6, 8],
    [8, 14, 11],
    [2, 4, 6]
]
main, secondary = diagonal_sums(matrix)

data = [
    ["Главная диагональ", "Побочная диагональ"],
    [main, secondary]
]
results = tabulate.tabulate(data)
print(results)
