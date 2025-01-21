def append_notes_to_file(notes, filename):
    try:
        with open('filename.txt', 'a', encoding='utf-8') as file:
            for note in notes:

                file.write(f"Имя пользователя: {note.get('user_name', 'Не указано')}\n")
                file.write(f"Заголовок: {note.get('title', 'Без заголовка')}\n")
                file.write(f"Описание заметки: {note.get('content', 'Без описания')}\n")
                file.write(f"Статус заметки: {note.get('status', 'Без статуса')}\n")
                file.write(f"Дата создания заметки: {note.get('created_date', 'Не указана')}\n")
                file.write(f"Истечение заметки: {note.get('issue_date', 'Не указано')}\n")
                file.write("---------------------\n")
                file.close()

    except FileNotFoundError:
        print("")
    except Exception as e:
        print(f"Ошибка при записи в файл: {filename}: {e}")
    return notes

if __name__ == '__main__':
    new_notes = [
        {
            "user_name": "Мария",
            "title": "План работы",
            "content": "Подготовить отчёт",
            "status": "в процессе",
            "created_date": "27.11.2024",
            "issue_date": "28.11.2024"
        }
    ]
    append_notes_to_file(new_notes, "notes.txt")
