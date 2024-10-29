# var1 = 5
# PI = 3.141592
#
# def func():
#     global var1
#     global PI
#     s = PI * var1**2
#     PI = 5.36
#     print(s)
#
#
# func()
# print(var1)
# print(PI)


import random

def game(user_choice):
    comp_choice = random.choice("KNB")
    user_choice = str.upper(user_choice)
    print(f"Гравець - {user_choice}, Комп'ютер - {comp_choice}")
    if user_choice == comp_choice:
        return "D"
    elif (user_choice == "K" and comp_choice == "N" or
          user_choice == "B" and comp_choice == "K" or
          user_choice == "N" and comp_choice == "B"):
        return "U"
    elif (comp_choice == "K" and user_choice == "N" or
          comp_choice == "B" and user_choice == "K" or
          comp_choice == "N" and user_choice == "B"):
        return "C"


def print_result(winner, result):
    if winner == "D":
        print("В цьому раунді нічья")
    elif winner == "U":
        print("В цьому раунді переміг гравець")
        result["user"] += 1
    elif winner == "C":
        print("В цьому раунді переміг комп'ютер")
        result["comp"] += 1
    print(f'Гравець - {result["user"]}, Комп\'ютер - {result["comp"]}')

def next_game():
    # return True False

result = {"user": 0, "comp": 0}

for i in range(1, 4):
    print(f"======= РАУНД №{i}=======")
    print_result(game(input("Виберіть K, N, B  - ")), result)
    print()