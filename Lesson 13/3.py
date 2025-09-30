class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        ingredients = []
        if self.cheese:
            ingredients.append("сыр")
        if self.pepperoni:
            ingredients.append("пепперони")
        if self.mushrooms:
            ingredients.append("грибы")
        if self.onions:
            ingredients.append("лук")
        if self.bacon:
            ingredients.append("бекон")

        ingredients_str = ", ".join(ingredients) if ingredients else "нет ингредиентов"
        return f"Пицца {self.size} см с: {ingredients_str}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self, size, *ingredients):
        builder = self.builder.set_size(size)

        ingredient_methods = {
            'cheese': builder.add_cheese,
            'pepperoni': builder.add_pepperoni,
            'mushrooms': builder.add_mushrooms,
            'onions': builder.add_onions,
            'bacon': builder.add_bacon
        }

        for ingredient in ingredients:
            if ingredient in ingredient_methods:
                ingredient_methods[ingredient]()

        return builder.build()

if __name__ == "__main__":
    # Использование строителя напрямую
    builder = PizzaBuilder()
    pizza1 = (builder
              .set_size(30)
              .add_cheese()
              .add_pepperoni()
              .add_mushrooms()
              .build())
    print("Пицца 1:", pizza1)

    # Использование директора
    builder2 = PizzaBuilder()
    director = PizzaDirector(builder2)

    pizza2 = director.make_pizza(25, 'cheese', 'bacon', 'onions')
    print("Пицца 2:", pizza2)

    pizza3 = director.make_pizza(35, 'cheese', 'pepperoni', 'mushrooms', 'bacon')
    print("Пицца 3:", pizza3)