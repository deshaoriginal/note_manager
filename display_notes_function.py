from colorama import init, Fore, Back

init(autoreset=True)

# Добавили библиотеку Colorama

def display_notes(notes):
    if not notes:
        print(Fore.RED + "У вас нет сохраненных заметок.")
    else:
        print(Fore.GREEN + "Список заметок:\n" + Back.YELLOW + "-" * 30)
        for index, note in enumerate(notes, start = 1):
            print(Fore.GREEN + f"Заметка №{index}:\n"
                  f"Имя пользователя: {note['user_name']}\n"
                  f"Заголовок: {note['title']}\n"
                  f"Описание: {note['content']}\n"
                  f"Статус: {note['status']}\n"
                  f"Дата создания: {note['created_date']}\n"
                  f"Дата истечения заметки: {note['issue_date']}\n"
                  + Back.YELLOW + "-" * 30)

# Пример использования функции display_notes

if __name__ == '__main__':
    test_notes  = [
        {
            "user_name": "Алексей",
            "title": "Список покупок",
            "content": "Купить продукты на неделю",
            "status": "новая",
            "created_date": "27-11-2024",
            "issue_date": "30-11-2024"
        },
        {
            "user_name": "Мария",
            "title": "Учеба",
            "content": "Подготовиться к экзамену",
            "status": "в процессе",
            "created_date": "25-11-2024",
            "issue_date": "01-12-2024"
        }
    ]

display_notes([])

# Вывод пустых заметок

display_notes(test_notes)

# Вывод примерных тестовых заметок
