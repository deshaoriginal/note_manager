def display_page(notes, page):
    start_index = 0 + page * 5
    end_index = 5 + page * 5
                                # notes[0:5] - первая страница
                                # notes[5:10] - вторая страница
    for index, note in enumerate(notes[start_index:end_index], start=1):  # f строки f string
        print(f"""
        Номер заметки: {index}
        Имя пользователя: {note["user_name"]}
        Заголовок: {note["title"]}
        """)
        print("_" * 80)  # str * int

def display_notes(notes, page_number=0):
    if not notes:
        print("Список заметок пуст")
    else:
        display_page(notes, page_number)

if __name__ == '__main__':
    notes = [
        {"user_name": "1", "title": "Y", "status": "F"},
        {"user_name": "2", "title": "CV"},
        {"user_name": "3", "title": "CV"},
        {"user_name": "4", "title": "CV"},
        {"user_name": "5", "title": "CV"},
        {"user_name": "6", "title": "CV"},
        {"user_name": "7", "title": "CV"},
        {"user_name": "8", "title": "CV"},
        {"user_name": "9", "title": "CV"},
        {"user_name": "10", "title": "CV"},
    ]
    display_notes(notes=notes, page_number=1)
