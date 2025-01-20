
def save_notes_to_file(notes, filename):
    
    with open('filename.txt', 'w+', encoding='utf-8') as file:
        for note in notes:

            file.write(f"Имя пользователя: {note.get('user_name', 'Не указано')}\n")
            file.write(f"Заголовок: {note.get('title', 'Без заголовка')}\n")
            file.write(f"Описание заметки: {note.get('content', 'Без описания')}\n")
            file.write(f"Статус заметки: {note.get('status', 'Без статуса')}\n")
            file.write(f"Дата создания заметки: {note.get('created_date', 'Не указана')}\n")
            file.write(f"Истечение заметки: {note.get('issue_date', 'Не указано')}\n")
            file.write("---------------------\n")

    file.close()

# Пример использования функции
notes = [
    {
        "user_name": "Денис",
        "title": "продукты",
        "content": "купить продукты на неделю",
        "status": "новая",
        "created_date": "20.1.2025",
        "issue_date": "23.1.2025"
    }
]
save_notes_to_file(notes, 'filename.txt')
