import random

def main():
    print("Камень, ножницы, бумага")
    select = input("Выберите: камень, ножницы или бумага: ").lower()

    allowed = ["камень", "ножницы", "бумага"]

    if select in allowed:
        bot = random.choice(allowed)
        print(f"Бот выбрал: {bot}")

        if bot == select:
            print("Ничья!")
        elif (select == "камень" and bot == "ножницы") or \
             (select == "ножницы" and bot == "бумага") or \
             (select == "бумага" and bot == "камень"):
            print("Вы выиграли!")
        else:
            print("Вы проиграли!")
    else:
        print("Неправильный выбор. Попробуйте снова.")

