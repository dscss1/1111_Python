#
# print(345,657,67,56,23,423,4345,4,56,568,679,789,567,3,454,254,66,7,689,9870,8,756,5)
#
# def func(*args):
#     for i in args:
#         print(i, end=', ')
#     print()
#
# func("mama",345,456,456,75,432,1,45,67897,654,423)
#
# def summ(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
# l = [345,456,456,75,432,1,45,67897,654,423]
#
# print(summ(*l))
#
# def func2(**kwargs):
#     for key in kwargs:
#         print(f"{key} - {kwargs[key]}")
#
#
# func2(name="Vasya", age=15, height=170)
#
# def func3(a, *args, **kwargs):
#     print(a)
#     for i in args:
#         print(i, end=', ')
#     print()
#     for key in kwargs:
#         print(f"{key} - {kwargs[key]}")
#
# func3(100, "ewe", "dwefwef", 234, age=15, name="Vasya")
import random

players = ['Serg', 'Anna', "Anton"]
list_question = ["Як тебе називають у школі?", "Хто твій найкращій друг?", "Як пройшов твій день?"]
list_action = ["Помий посуд", "Сходи за хлібом", "Зроби ДЗ"]

def get_players(players):
    while True:
        name = input("Введіть ім'я гравця : ")
        players.append(name)
        if len(players) < 2:
            continue
        else:
            next = input("Чи хочете ще додати гравця? (Y/N) : ")
            if str.upper(next) == "Y":
                continue
            else:
                break

def game(list_action, list_question, players):
    for name in players:
        choice = input(f"Вибір для гравця {name}: Правда або Дія (P/D) : ")
        if str.upper(choice) == "P":
            index = random.randint(0, len(list_question) - 1)
            print(list_question[index])
            list_question.pop(index)
        elif str.upper(choice) == "D":
            index = random.randint(0, len(list_action) - 1)
            print(list_action[index])
            list_action.pop(index)





#get_players(players)
while True:
    if game(list_action, list_question, players) == False:
        print("Вибачте, в нас закінчились питання.")
        break


# dic = {}
# dic[name] = superHero