import random

def main():
    print("Камень, ножницы, бумага")

    rounds = int(input("Сколько раундов вы хотите сыграть? "))
    player_score = 0
    bot_score = 0

    allowed = ["камень", "ножницы", "бумага"]

    for round_num in range(1, rounds + 1):
        print(f"\nРаунд {round_num}")
        user_choice = input("Выберите: камень, ножницы или бумага: ").lower()

        if user_choice not in allowed:
            print("Неправильный выбор. Попробуйте снова.")
            continue

        bot = random.choice(allowed)
        print(f"Бот выбрал: {bot.upper}")

        if bot == user_choice:
            print("Ничья!")
        elif (user_choice == "камень" and bot == "ножницы") or \
                (user_choice == "ножницы" and bot == "бумага") or \
                (user_choice == "бумага" and bot == "камень"):
            print("Вы выиграли раунд!")
            player_score += 1
        else:
            print("Бот выиграл раунд!")
            bot_score += 1

        print(f"Текущий счёт - Вы: {player_score}, Бот: {bot_score}")

    print("\nИгра завершена!")
    print(f"Итоговый счёт - Вы: {player_score}, Бот: {bot_score}")

    if player_score > bot_score:
        print("Поздравляем, вы выиграли игру!")
    elif player_score < bot_score:
        print("К сожалению, бот выиграл игру.")
    else:
        print("Игра закончилась вничью!")



