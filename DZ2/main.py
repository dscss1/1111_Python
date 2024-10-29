import random

def random_number():
    min_value = int(input("Введіть найменше значення: "))
    max_value = int(input("Введіть найбільше значення: "))
    number = random.randint(min_value, max_value)
    print(f"Випадкове число з діапазону ({min_value}, {max_value}): {number}")

def main():
    random_number()
