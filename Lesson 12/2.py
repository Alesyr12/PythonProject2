class PcheloSlon:
    def __init__(self, pchela, slon):
        self.pchela = pchela
        self.slon = slon

    def fly(self):
        if self.pchela >= self.slon:
            return True
        else:
            return False

    def trumpet(self):
        if self.slon >= self.pchela:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            # Вычитаем у слона, добавляем пчеле
            self.slon -= value
            self.pchela += value
        elif meal == "grass":
            # Вычитаем у пчелы, добавляем слону
            self.pchela -= value
            self.slon += value
        else:
            print("Ошибка! Можно есть только nectar или grass")
            return

        # Проверяем чтобы не было меньше 0
        if self.pchela < 0:
            self.pchela = 0
        if self.slon < 0:
            self.slon = 0

        # Проверяем чтобы не было больше 100
        if self.pchela > 100:
            self.pchela = 100
        if self.slon > 100:
            self.slon = 100


# Проверяем как работает
print("Создаем ПчёлоСлона: пчела=60, слон=70")
zhivotnoe = PcheloSlon(60, 70)

print(f"Может летать? {zhivotnoe.fly()}")
print(f"Звук: {zhivotnoe.trumpet()}")
print()

print("ПчёлоСлон ест nectar на 40:")
zhivotnoe.eat("nectar", 40)
print(f"Теперь пчела={zhivotnoe.pchela}, слон={zhivotnoe.slon}")

print(f"Может летать? {zhivotnoe.fly()}")
print(f"Звук: {zhivotnoe.trumpet()}")
print()

print("ПчёлоСлон ест grass на 10:")
zhivotnoe.eat("grass", 10)
print(f"Теперь пчела={zhivotnoe.pchela}, слон={zhivotnoe.slon}")

print(f"Может летать? {zhivotnoe.fly()}")
print(f"Звук: {zhivotnoe.trumpet()}")
print()

print("Пробуем съесть что-то непонятное:")
zhivotnoe.eat("мясо", 20)