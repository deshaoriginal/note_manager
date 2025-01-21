from logging import exception


def save_notes_to_file(notes, filename):
    try:
        with open('filename.txt', 'w+', encoding='utf-8') as file:
            for note in notes:

                file.write(f"Имя пользователя: {note.get('user_name', 'Не указано')}\n")
                file.write(f"Заголовок: {note.get('title', 'Без заголовка')}\n")
                file.write(f"Описание заметки: {note.get('content', 'Без описания')}\n")
                file.write(f"Статус заметки: {note.get('status', 'Без статуса')}\n")
                file.write(f"Дата создания заметки: {note.get('created_date', 'Не указана')}\n")
                file.write(f"Истечение заметки: {note.get('issue_date', 'Не указано')}\n")
                file.write("---------------------\n")
    except FileNotFoundError:
        print("")
    except Exception as e:
        print(f"Ошибка при записи в файл: {filename}: {e}")
    return notes

# Пример использования функции
notes = [
    {
        "user_name": "Денис",
        "title": "продукты",
        "content": "купить продукты на неделю",
        "status": "новая",
        "created_date": "20.1.2025",
        "issue_date": "23.1.2025"
    },
    {
        "user_name": "Алексей",
        "title": "Список покупок",
        "content": "Купить продукты",
        "status": "новая",
        "created_date": "27.11.2024",
        "issue_date": "30.11.2024"

    }
]
if __name__ == '__main__':
    save_notes_to_file(notes, 'filename.txt')
