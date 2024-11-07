import math

# Функція для обчислення об'єму прямої зрізаної піраміди
def calculate_volume(a1, a2, h):
    # Площа основ: формула для площі правильного трикутника
    area1 = (math.sqrt(3) / 4) * (a1 ** 2)
    area2 = (math.sqrt(3) / 4) * (a2 ** 2)
    # Формула для об'єму зрізаної піраміди
    volume = (1 / 3) * h * (area1 + area2 + math.sqrt(area1 * area2))
    return volume

# Функція для обчислення площі поверхні прямої зрізаної піраміди
def calculate_surface_area(a1, a2, h):
    # Площа основ
    area1 = (math.sqrt(3) / 4) * (a1 ** 2)
    area2 = (math.sqrt(3) / 4) * (a2 ** 2)
    # Висота бічної сторони піраміди
    slant_height = math.sqrt(h ** 2 + ((a1 - a2) / 2) ** 2)
    # Периметри основ
    perimeter1 = 3 * a1
    perimeter2 = 3 * a2
    # Площа бічної поверхні
    lateral_area = (perimeter1 + perimeter2) * slant_height / 2
    # Загальна площа поверхні
    surface_area = area1 + area2 + lateral_area
    return surface_area
