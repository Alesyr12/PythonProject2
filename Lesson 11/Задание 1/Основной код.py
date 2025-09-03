class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def __str__(self):
        if self.taste:
            return f"У вас газировка с {self.taste} вкусом"
        return "У вас обычная газировка"


# Самый простой ввод
taste_input = input("Введите вкус газировки в творительном падеже (или Enter для обычной): ").strip()
my_soda = Soda(taste_input if taste_input else None)

print(my_soda)