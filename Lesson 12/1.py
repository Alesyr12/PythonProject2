# Класс для товара
class Tovar:
    def __init__(self, name, magazin, price):
        self.__name = name  # название товара
        self.__magazin = magazin  # магазин
        self.__price = price  # цена

    def get_name(self):
        return self.__name

    def get_magazin(self):
        return self.__magazin

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"Товар: {self.__name}, Магазин: {self.__magazin}, Цена: {self.__price} руб."

    def __add__(self, other):
        return self.__price + other.__price


# Класс для склада
class Sklad:
    def __init__(self):
        self.__tovary = []  # тут будут храниться все товары

    def dobavit_tovar(self, tovar):
        self.__tovary.append(tovar)
        print(f"Добавили товар {tovar.get_name()} на склад")

    def pokazat_vse_tovary(self):
        print("Все товары на складе:")
        for i, tovar in enumerate(self.__tovary):
            print(f"{i}: {tovar}")
        print()

    def naiti_po_nomeru(self, nomer):
        if nomer < 0 or nomer >= len(self.__tovary):
            print("Ошибка! Такого номера нет")
            return None
        print(f"Товар под номером {nomer}:")
        print(self.__tovary[nomer])
        return self.__tovary[nomer]

    def naiti_po_imeni(self, imya):
        for tovar in self.__tovary:
            if tovar.get_name() == imya:
                print(f"Нашли товар '{imya}':")
                print(tovar)
                return tovar
        print(f"Товар '{imya}' не найден")
        return None

    def sortirovat_po_nazvaniyu(self):
        self.__tovary.sort(key=lambda x: x.get_name())
        print("Отсортировали по названию товара")

    def sortirovat_po_magazinu(self):
        self.__tovary.sort(key=lambda x: x.get_magazin())
        print("Отсортировали по названию магазина")


    def sortirovat_po_cene(self):
        self.__tovary.sort(key=lambda x: x.get_price())
        print("Отсортировали по цене")

    def __add__(self, other):
        vsego = 0
        for tovar in self.__tovary:
            vsego += tovar.get_price()
        for tovar in other.__tovary:
            vsego += tovar.get_price()
        return vsego


if __name__ == "__main__":
    print("=== ПРОГРАММА ДЛЯ СКЛАДА ===")
    print()

    print("Создаем товары...")
    tovar1 = Tovar("Телефон", "Эльдорадо", 15000)
    tovar2 = Tovar("Наушники", "М-Видео", 3000)
    tovar3 = Tovar("Ноутбук", "Эльдорадо", 50000)
    tovar4 = Tovar("Мышь", "DNS", 800)

    sklad1 = Sklad()

    sklad1.dobavit_tovar(tovar1)
    sklad1.dobavit_tovar(tovar2)
    sklad1.dobavit_tovar(tovar3)
    sklad1.dobavit_tovar(tovar4)
    print()

    sklad1.pokazat_vse_tovary()

    sklad1.naiti_po_nomeru(1)
    print()

    sklad1.naiti_po_imeni("Ноутбук")
    sklad1.naiti_po_imeni("Принтер")  # такого нет
    print()

    sklad1.sortirovat_po_cene()
    sklad1.pokazat_vse_tovary()

    sklad1.sortirovat_po_nazvaniyu()
    sklad1.pokazat_vse_tovary()
    print()

    print("Создаем второй склад...")
    sklad2 = Sklad()
    tovar5 = Tovar("Клавиатура", "Ситилинк", 2500)
    tovar6 = Tovar("Колонки", "М-Видео", 4000)
    sklad2.dobavit_tovar(tovar5)
    sklad2.dobavit_tovar(tovar6)
    print()

    print("Сумма всех товаров на двух складах:")
    obshaya_cena = sklad1 + sklad2
    print(f"Общая стоимость: {obshaya_cena} руб.")
    print()

    print("Сумма цен телефона и ноутбука:")
    summa_dvuh = tovar1 + tovar3
    print(f"Телефон + Ноутбук = {summa_dvuh} руб.")

    print("\n=== ПРОГРАММА ЗАВЕРШЕНА ===")