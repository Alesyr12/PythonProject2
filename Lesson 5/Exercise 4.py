a1 = a2 = 1

n = int(input("Ввидите количество числе в ряду: "))

print(a1, a2, end=' ')

for i in range(2, n):
    a1, a2 = a2, a1 + a2
    print(a2, end=' ')