import random

heroes = [
    'Спайдермен', 'Супермен', 'Жінка-кішка', 'Бетмен', 
    'Залізна людина', 'Халк', 'Капітан Америка', 'Чорна вдова'
]

players = {}

def assign_hero(player_name):
    if len(players) >= len(heroes):
        print("Вибачте, всі ролі вже розподілені!")
        return
    
    hero = random.choice(heroes)
    heroes.remove(hero)
    players[player_name] = hero

def display_players():
    print("\nГравці та їхні супергерої:")
    for player, hero in players.items():
        print(f"{player} - {hero}")

def main():
    while True:
        player_name = input("Введіть своє ім'я (або 'вихід' для завершення): ").strip()
        if player_name.lower() == 'вихід':
            break
        elif player_name in players:
            print("Це ім'я вже використовується! Спробуйте інше.")
        else:
            assign_hero(player_name)
    
    display_players()