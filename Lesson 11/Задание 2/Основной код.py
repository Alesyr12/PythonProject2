class Math:
    def __init__(self):
        # Нет атрибутов при инициализации
        pass

    def addition(self, a, b):
        """Сложение двух чисел"""
        result = a + b
        print(f"{a} + {b} = {result}")
        return result

    def subtraction(self, a, b):
        """Вычитание двух чисел"""
        result = a - b
        print(f"{a} - {b} = {result}")
        return result

    def multiplication(self, a, b):
        """Умножение двух чисел"""
        result = a * b
        print(f"{a} * {b} = {result}")
        return result

    def division(self, a, b):
        """Деление двух чисел"""
        if b == 0:
            print("Ошибка: деление на ноль!")
            return None
        result = a / b
        print(f"{a} / {b} = {result}")
        return result


# Пример использования
if __name__ == "__main__":
    # Создаем объект класса Math
    calculator = Math()

    calculator.addition(10, 5)  # 10 + 5 = 15
    calculator.subtraction(10, 5)  # 10 - 5 = 5
    calculator.multiplication(10, 5)  # 10 * 5 = 50
    calculator.division(10, 5)  # 10 / 5 = 2.0
