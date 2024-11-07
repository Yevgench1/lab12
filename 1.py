def save_keys(input_file, output_file):
    keys = []
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            key, value = line.strip().split(": ")
            keys.append(key)
    with open(output_file, "w", encoding="utf-8") as file:
        for key in keys:
            file.write(key + "\n")

def display_unique_values(input_file):
    values = set()
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            key, value = line.strip().split(": ")
            values.add(value)
    print("Унікальні значення:", values)

input_file = "dictionary.txt"
output_file = "keys_list.txt"
save_keys(input_file, output_file)
display_unique_values(input_file)

