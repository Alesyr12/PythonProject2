from collections import Counter
import tabulate

numbers = [1, 2, 2, 6, 6, 3, 3, 4, 5, 123, 98, 98, 99, 123]
unique_numbers = list(set(numbers))
print(f'Сведения об уникальных значениях в списке \n{unique_numbers}')

def find_duplicates(numbers):
    counter = Counter(numbers)
    return [letter for letter in counter if counter[letter] > 1]
duplicates = f'Сведения о дубликатах в списке:  \n{find_duplicates(numbers)}'
print(duplicates)

char_counts_1 = numbers.count(2)
char_counts_2 = numbers.count(6)
char_counts_3 = numbers.count(3)
char_counts_4 = numbers.count(123)
char_counts_5 = numbers.count(98)

print('Сведения о количестве повторяющихся цифр с писке')
data = [
    ["2", "6", "3", "123", "98"],
    [char_counts_1, char_counts_2, char_counts_3, char_counts_4, char_counts_5]
]
results = tabulate.tabulate(data)
print(results)