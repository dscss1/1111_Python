import random

def corrector(string, width, symbol):
    return string.center(width, symbol)

def play_round():
    allowed = ["камінь", "ножиці", "папір", "ящірка", "спок"]
    user_choice = input(corrector("Виберіть: камінь, ножиці, папір, ящірка або Спок", 50, "=") + ": ").lower()

    if user_choice not in allowed:
        print(corrector("Неправильний вибір. Спробуйте знову.", 50, "-"))
        return 0, 0

    bot_choice = random.choice(allowed)
    print(corrector(f"Бот вибрав: {bot_choice}", 50, "-"))

    if bot_choice == user_choice:
        print(corrector("Нічия!", 50, "-"))
        return 0, 0
    elif (user_choice == "камінь" and (bot_choice == "ножиці" or bot_choice == "ящірка")) or \
         (user_choice == "ножиці" and (bot_choice == "папір" or bot_choice == "ящірка")) or \
         (user_choice == "папір" and (bot_choice == "камінь" or bot_choice == "спок")) or \
         (user_choice == "ящірка" and (bot_choice == "папір" or bot_choice == "спок")) or \
         (user_choice == "спок" and (bot_choice == "камінь" or bot_choice == "ножиці")):
        print(corrector("Ви виграли раунд!", 50, "-"))
        return 1, 0
    else:
        print(corrector("Бот виграв раунд!", 50, "-"))
        return 0, 1

def main():
    player_score = 0
    bot_score = 0

    while player_score < 3 and bot_score < 3:
        p, b = play_round()
        player_score += p
        bot_score += b
        print(corrector(f"Текущий счёт - Ви: {player_score}, Бот: {bot_score}", 50, "="))

    if player_score > bot_score:
        print(corrector("Вітаємо, ви виграли гру!", 50, "="))
    else:
        print(corrector("На жаль, бот виграв гру.", 50, "="))

if __name__ == "__main__":
    main()
