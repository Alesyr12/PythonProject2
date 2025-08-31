class Avtobus:
    def __init__(self, max_mesta, max_skorost):
        self.skorost = 0
        self.max_mesta = max_mesta
        self.max_skorost = max_skorost
        self.passazhiri = []
        self.mesta = {}

    @property
    def est_svobodnie_mesta(self):
        return len(self.passazhiri) < self.max_mesta

    def posadka(self, familiya):
        if not self.est_svobodnie_mesta:
            return False
        self.passazhiri.append(familiya)
        for i in range(1, self.max_mesta + 1):
            if i not in self.mesta:
                self.mesta[i] = familiya
                return True

    def vysadka(self, familiya):
        if familiya not in self.passazhiri:
            return False
        self.passazhiri.remove(familiya)
        for mesto, fam in list(self.mesta.items()):
            if fam == familiya:
                del self.mesta[mesto]
                return True

    def izmenit_skorost(self, delta):
        self.skorost = max(0, min(self.skorost + delta, self.max_skorost))
        return self.skorost

    def __contains__(self, familiya):
        return familiya in self.passazhiri

    def __iadd__(self, familiya):
        self.posadka(familiya)
        return self

    def __isub__(self, familiya):
        self.vysadka(familiya)
        return self

    def __str__(self):
        return f"Автобус: {len(self.passazhiri)}/{self.max_mesta} пасс., {self.skorost} км/ч"


# Проверка
avtobus = Avtobus(13, 150)
print(avtobus)

avtobus += "Гладков"
avtobus += "Смирнов"
print(avtobus)
print("Свободные места:", avtobus.est_svobodnie_mesta)

avtobus.izmenit_skorost(90)
print(avtobus)

print("Гладков в автобусе?", "Гладков" in avtobus)

avtobus -= "Гладков"
print(avtobus)