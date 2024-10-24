import os
import importlib.util
import sys

import art
from art import text2art, tprint

root_dir = os.getcwd()


def get_folders():
    folders = [f for f in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, f)) and not f.startswith('.')]
    return folders


def create_main_py(folder):
    main_file_path = os.path.join(root_dir, folder, "main.py")
    with open(main_file_path, 'w', encoding='utf-8') as f:
        f.write("def main():\n")
        f.write("    print('Привет, мир!')\n")
        f.write("\nif __name__ == '__main__':\n")
        f.write("    main()\n")
    print(f"Файл {main_file_path} успешно создан.")


def run_main_py(folder):
    main_file_path = os.path.join(root_dir, folder, "main.py")
    spec = importlib.util.spec_from_file_location("main", main_file_path)
    main_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main_module)

    if hasattr(main_module, 'main'):
        main_module.main()
    else:
        print(f"Функция 'main' не найдена в {main_file_path}.")


if __name__ == "__main__":
    folders = get_folders()
    try:
        user = os.getlogin()
    except OSError:
        user = os.getenv('USER', 'Пользователь')

    Art = text2art("Selector", font='block', chr_ignore=True)

    print(Art)
    tprint('Powered by Sergey Karmazin')

    print(f"Добро пожаловать, {user}")


    print("Доступные уроки:")
    for i, folder in enumerate(folders, start=1):
        print(f"- {i}. {folder}")
    try:
        select = int(input("$ "))
    except Exception as e:
        print(e)
        sys.exit(0)

    if 1 <= select <= len(folders):
        selected_folder = folders[select - 1]
        main_file_path = os.path.join(root_dir, selected_folder, "main.py")

        if os.path.isfile(main_file_path):
            print(f"Файл {main_file_path} найден.")
            run_main_py(selected_folder)
        else:
            print(f"Файл {main_file_path} не найден.")
            create_main = input("Файл main.py не найден. Хотите создать его? (да/нет): ").strip().lower()
            if create_main == 'да':
                create_main_py(selected_folder)
                run_main_py(selected_folder)
            else:
                print("Файл не был создан.")
    else:
        print("Некорректный номер урока.")
