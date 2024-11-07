import random

def generate_engine_number():
    digits = "".join([str(random.randint(0, 9)) for _ in range(7)])
    year = random.randint(2000, 2022)
    return f"{digits}-{year}"

def save_engine_numbers(filename, n):
    numbers = set()
    with open(filename, "w", encoding="utf-8") as file:
        for _ in range(n):
            number = generate_engine_number()
            numbers.add(number)
            file.write(number + "\n")
    print(f"Кількість унікальних номерів: {len(numbers)}")

filename = "engine_numbers.txt"
N = 100 
save_engine_numbers(filename, N)
