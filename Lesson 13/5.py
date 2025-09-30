from abc import ABC, abstractmethod


# Абстрактный класс стратегии
class MathStrategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


# Конкретные стратегии математических операций
class Addition(MathStrategy):
    def execute(self, a, b):
        return a + b

    def __str__(self):
        return "сложение"


class Subtraction(MathStrategy):
    def execute(self, a, b):
        return a - b

    def __str__(self):
        return "вычитание"


class Multiplication(MathStrategy):
    def execute(self, a, b):
        return a * b

    def __str__(self):
        return "умножение"


class Division(MathStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("ЗАМОНИ ДЕЛИТЬ НА 0 НЕЛЬЗЯ!")
        return a / b

    def __str__(self):
        return "деление"


class Power(MathStrategy):
    def execute(self, a, b):
        return a ** b

    def __str__(self):
        return "возведение в степень"


# Класс Calculator, использующий стратегии
class Calculator:
    def __init__(self, strategy=None):
        # По умолчанию используем сложение
        self._strategy = strategy or Addition()

    def set_strategy(self, strategy):
        """Устанавливает текущую стратегию"""
        if not isinstance(strategy, MathStrategy):
            raise TypeError("Стратегия должна наследоваться от MathStrategy")
        self._strategy = strategy
        return self

    def calculate(self, a, b):
        """Выполняет операцию с помощью текущей стратегии"""
        if self._strategy is None:
            raise ValueError("Стратегия не установлена")

        result = self._strategy.execute(a, b)
        return result

    def get_current_strategy(self):
        """Возвращает текущую стратегию"""
        return self._strategy


# Демонстрация использования
if __name__ == "__main__":
    print("=== Калькулятор с паттерном Стратегия ===\n")

    # Создаем калькулятор
    calculator = Calculator()

    # Тестовые числа
    a, b = 10, 4

    # Используем разные стратегии
    strategies = [
        Addition(),
        Subtraction(),
        Multiplication(),
        Division(),
        Power()
    ]

    print(f"Вычисления для чисел {a} и {b}:\n")

    for strategy in strategies:
        calculator.set_strategy(strategy)
        try:
            result = calculator.calculate(a, b)
            print(f"{strategy}: {a} и {b} = {result}")
        except ValueError as e:
            print(f"{strategy}: {a} и {b} = Ошибка: {e}")

    print("\n=== Динамическое переключение стратегий ===")

    # Демонстрация динамического изменения стратегии
    calculator.set_strategy(Addition())
    print(f"\nТекущая стратегия: {calculator.get_current_strategy()}")
    print(f"10 + 4 = {calculator.calculate(10, 4)}")

    calculator.set_strategy(Multiplication())
    print(f"\nТекущая стратегия: {calculator.get_current_strategy()}")
    print(f"10 * 4 = {calculator.calculate(10, 4)}")

    print("\n=== Обработка ошибок ===")

    # Тестирование деления на ноль
    calculator.set_strategy(Division())
    try:
        result = calculator.calculate(10, 0)
    except ValueError as e:
        print(f"{e}")

    print("\n=== РЕЖИМ ТЕСТИРОВАНИЯ ===")

    calc = Calculator(Addition())

    operations = {
        '+': Addition(),
        '-': Subtraction(),
        '*': Multiplication(),
        '/': Division(),
        '^': Power()
    }

    while True:
        print("\nМетод вычесления: +, -, *, /, ^ (или 'quit' для выхода)")
        op = input("Выберите операцию: ").strip()

        if op.lower() == 'quit':
            break

        if op not in operations:
            print("Неизвестная операция!")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            calc.set_strategy(operations[op])
            result = calc.calculate(num1, num2)
            print(f"Результат: {num1} {op} {num2} = {result}")

        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except Exception as e:
            print(f"Ошибка вычисления: {e}")