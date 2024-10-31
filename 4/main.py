import json

players = []
file_path = './4/allowed.json'


def load_questions_and_actions(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            questions = data.get("questions", [])
            actions = data.get("actions", [])
            return questions, actions
    except FileNotFoundError:
        print("Файл не найден. Проверьте путь к файлу.")
        return [], []
    except json.JSONDecodeError:
        print("Ошибка в формате JSON. Проверьте содержимое файла.")
        return [], []


questions, actions = load_questions_and_actions(file_path)


def main():
    try:
        num_players = int(input("Введите количество игроков: "))
    except ValueError:
        print("Пожалуйста, введите корректное число.")
        return
    if num_players < 2:
        print("Вас слишком мало, минимум 2 игрока.")
        return
    for i in range(1, num_players + 1):
        name = input(f"Введите имя игрока {i}: ")
        players.append(name)
    if players and questions and actions:
        game = Game(players, actions, questions)
        game.start()
    else:
        print("Игра не может начаться: недостаточно игроков, вопросов или действий.")


class Game:
    def __init__(self, players, actions, questions):
        self.players = players
        self.actions = actions
        self.questions = questions
        self.game_over = False

    def start(self):
        print("Игра началась!")
        player_index = 0
        while not self.game_over:
            self.game_cycle(player_index)
            player_index = (player_index + 1) % len(self.players)

    def game_cycle(self, player_index):
        current_player = self.players[player_index]
        print(f"\nХод игрока: {current_player}")

        while True:
            choice = input("Выберите 'правда', 'действие', 'скип' или 'перезагрузить': ").strip().lower()

            if choice == "правда":
                if self.questions:
                    print(f"Вопрос для {current_player}: {self.questions.pop(0)}")
                else:
                    print("Вопросы закончились! Игра завершена.")
                    self.game_over = True
                break
            elif choice == "действие":
                if self.actions:
                    print(f"Действие для {current_player}: {self.actions.pop(0)}")
                else:
                    print("Действия закончились! Игра завершена.")
                    self.game_over = True
                break
            elif choice == "скип":
                print(f"{current_player} пропустил ход.")
                break
            elif choice == "перезагрузить":
                self.reload_config()
                print("Конфигурация перезагружена!")
            else:
                print("Некорректный выбор. Попробуйте снова.")

    def reload_config(self):
        global questions, actions
        questions, actions = load_questions_and_actions(file_path)
        self.questions = questions
        self.actions = actions
