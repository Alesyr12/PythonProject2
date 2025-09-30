from abc import ABC, abstractmethod


# Абстрактный класс Animal
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# Конкретные классы животных
class Dog(Animal):
    def speak(self):
        return "Гав-гав!"

    def __str__(self):
        return "Собака"


class Cat(Animal):
    def speak(self):
        return "Мяу-мяу!"

    def __str__(self):
        return "Кот"


# Фабричный метод
class AnimalFactory:
    def create_animal(self, animal_type):
        animal_type = animal_type.lower().strip()

        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")


# Альтернативная реализация с использованием словаря
class AnimalFactoryV2:
    def __init__(self):
        self._animals = {
            "dog": Dog,
            "cat": Cat
        }

    def create_animal(self, animal_type):
        animal_type = animal_type.lower().strip()

        if animal_type in self._animals:
            return self._animals[animal_type]()
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")

    def register_animal(self, animal_type, animal_class):
        """Метод для регистрации новых типов животных"""
        self._animals[animal_type.lower()] = animal_class


# Демонстрация использования
if __name__ == "__main__":
    print("=== Фабрика животных ===")

    # Использование базовой фабрики
    factory = AnimalFactory()

    # Создание собаки
    dog = factory.create_animal("dog")
    print(f"{dog}: {dog.speak()}")

    # Создание кота
    cat = factory.create_animal("cat")
    print(f"{cat}: {cat.speak()}")

