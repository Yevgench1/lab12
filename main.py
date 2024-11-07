import pyramid

a1 = float(input("Введіть довжину сторони нижньої основи (a1): "))
a2 = float(input("Введіть довжину сторони верхньої основи (a2): "))
h = float(input("Введіть висоту піраміди (h): "))

volume = pyramid.calculate_volume(a1, a2, h)
surface_area = pyramid.calculate_surface_area(a1, a2, h)

print(f"Об'єм прямої зрізаної піраміди: {volume}")
print(f"Площа поверхні прямої зрізаної піраміди: {surface_area}")
