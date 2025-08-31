from functools import reduce

# Указываем вводные значения, где слова 'length' и 'width' будут ключевыми для функций
rooms = [
    {'name': 'Kitchen', 'length': 15, 'width': 23},
    {'name': 'Room 1', 'length': 4.3, 'width': 4.2},
    {'name': 'Room 2', 'length': 4, 'width': 3.5},
    {'name': 'Room 3', 'length': 3.2, 'width': 1.8}
]

# Делаем функцию для вычесления площади
def calculate_area(room):
    return room['length'] * room['width']

# Посредством map() вычисляем площадь каждой комнаты
areas = list(map(calculate_area, rooms))

# Посредством reduce() считаем всю площадь квартиры
total_area = reduce(lambda x, y: x + y, areas)
for room, area in zip(rooms, areas):
    print(f"{room['name']}: {area:.1f} м² ")
print(f"Общая площадь квартиры: {total_area:.2f} м²")