# Делаем ввод списка вручную
numbers = input("Введите список чисел, разделенных пробелом: ").split()
print(list(map(str, numbers)))