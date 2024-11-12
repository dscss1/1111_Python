import random

def insert_random_symbol(string, symbols):
    position = random.randint(0, len(string))
    symbol = random.choice(symbols)
    new_string = string[:position] + symbol + string[position:]
    return new_string

symbols = ["!", "@", "#", "$", "%"]
user_string = input("Введіть рядок: ")
print(insert_random_symbol(user_string, symbols))
