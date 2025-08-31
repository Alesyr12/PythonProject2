'''
 item - искомое значение
 binary_search - функция, осуществляющее поиск искомого значения
 numbers - списко, в котором будет осуществляться поиск элемента
 '''
def binary_search(numbers, item):

# Устанавливаем начальный и конечный элемент
    first = 0
    last = len(numbers) - 1

    while first <= last:
        #Оперделяем среднее значение
        mid = (first + last) // 2

        if numbers[mid] == item:
            return mid

        # Если среднее значение больше искомого:
        elif numbers[mid] > item:
            last = mid - 1

        # Если средний элемент меньше искомго:
        else:
            first = mid + 1

    return None


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(binary_search(numbers, 5))