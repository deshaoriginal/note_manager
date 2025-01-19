def search_notes(notes, keyword = None, status = None):

# Функция поиска заметок по ключевому слову и\или статусу

    filtered_notes = []

    for note in notes:
        matches_keyword = False
        matches_status = False

        if keyword:

# Проверяем, встречается ли ключевое слово

            if (keyword.lower() in note.get('title', '').lower() or
                keyword.lower() in note.get('content', '').lower() or
                keyword.lower() in note.get('user_name', '').lower()):
                matches_keyword = True

        if status:

# Проверяем, совпадает ли статус

            if status.lower() == note.get('status', '').lower():
                matches_status = True

# Определяем, нужно ли добавить заметку в результат

        if (keyword and status and matches_keyword and matches_status) or \
            (keyword and not status and matches_keyword) or \
            (status and not keyword and matches_status):
            filtered_notes.append(note)

        elif not keyword and not status:
            filtered_notes.append(note)

# Вывод результатов

    if filtered_notes:
        print("Найдены заметки:")
        for i, note in enumerate(filtered_notes, 1):
            print(f"Заметка №{i}:")
            print(f"Имя пользователя: {note['user_name']}")
            print(f"Заголовок: {note['title']}")
            print(f"Описание: {note['content']}")
            print(f"Статус: {note['status']}\n")

    else:
        print("Заметки, соответствующие запросу , не найдены.")

# Пример использования функции

notes = [

    {'user_name': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27.11.2024', 'issue_date': '30.11.2024'},
    {'user_name': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе', 'created_date': '25.11.2024', 'issue_date': '01.12.2024'},
    {'user_name': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено', 'created_date': '20.11.2024', 'issue_date': '26.11.2024'}

    ]

# Вызов функций для примера

search_notes(notes, keyword = 'покупок')
search_notes(notes, status = 'в процессе')
search_notes(notes, keyword = 'работы', status = 'выполнено')
search_notes([])
search_notes(notes, keyword = 'больница')

