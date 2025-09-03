class SuperStr(str):
    def is_repeatance(self, s):

        if not isinstance(s, str) or len(s) == 0 or len(self) == 0:
            return False
        if len(self) % len(s) != 0:
            return False
        repeat_count = len(self) // len(s)
        return self == s * repeat_count

    def is_palindrom(self):
        s = self.lower()
        return s == s[::-1]

s = SuperStr("sdsdffrrrssdfffsa")
print(s.is_repeatance("abb"))
print(s.is_repeatance("ac"))

p = SuperStr("Firch")
print(p.is_palindrom())
print(SuperStr("World Heelo ").is_palindrom())
print(SuperStr("").is_palindrom())