n = int(input('Стоимость мобильного телефона: '))
k = int(input('Сумма откладываемая каждый день: '))

days = 0
money = 0

while money < n:
    days += 1
    if days %7  != 0:
        money += k
print("Маша накопит нужную сумму {} дней".format(days))