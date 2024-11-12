import random

def main():
    print("Камінь, ножиці, папір, ящірка, Спок")

    while True:
        player_score = 0
        bot_score = 0

        allowed = ["камінь", "ножиці", "папір", "ящірка", "спок"]

        while player_score < 3 and bot_score < 3:
            user_choice = input("Виберіть: камінь, ножиці, папір, ящірка або Спок: ").lower()

            if user_choice not in allowed:
                print("Неправильний вибір. Спробуйте знову.")
                continue

            bot_choice = random.choice(allowed)
            print(f"Бот вибрав: {bot_choice}")

            if bot_choice == user_choice:
                print("Нічия!")
            elif (user_choice == "камінь" and (bot_choice == "ножиці" or bot_choice == "ящірка")) or \
                 (user_choice == "ножиці" and (bot_choice == "папір" or bot_choice == "ящірка")) or \
                 (user_choice == "папір" and (bot_choice == "камінь" or bot_choice == "спок")) or \
                 (user_choice == "ящірка" and (bot_choice == "папір" or bot_choice == "спок")) or \
                 (user_choice == "спок" and (bot_choice == "камінь" or bot_choice == "ножиці")):
                print("Ви виграли раунд!")
                player_score += 1
            else:
                print("Бот виграв раунд!")
                bot_score += 1

            print(f"Текущий счёт - Ви: {player_score}, Бот: {bot_score}")

        if player_score > bot_score:
            print("Вітаємо, ви виграли гру!")
        else:
            print("На жаль, бот виграв гру.")

        play_again = input("Бажаєте зіграти ще раз? (так/ні): ").lower()
        if play_again != "так":
            break

if __name__ == "__main__":
    main()
