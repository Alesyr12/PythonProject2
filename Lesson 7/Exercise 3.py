# Создаем функцию для проверки, читается ли слово одинаково справа и слева
def function(s):
    return s == s[::-1]

words = ["deed", "deified", "hello", "word", "sagas", "man", "dog"]
palindromes = list(filter(function, words))
print(palindromes)