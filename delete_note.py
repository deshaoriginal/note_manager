
# Программа, которая предоставляет пользователю возможность удалить заметку из списка заметок.

def display_notes(notes):

    if not notes:
        print("В данный момент заметок нет.")
    else:
        print("Текущие заметки:")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. Имя: {note['name']}\n   Заголовок: {note['title']}\n   Описание: {note['description']}\n")

def delete_notes(notes, criterion):
    original_count = len(notes)
    notes[:] = [note for note in notes if note['name'].lower() != criterion.lower() and note['title'].lower() != criterion.lower()]
    deleted_count = original_count - len(notes)
    if deleted_count == 0:
        print("Заметок с таким именем пользователя или заголовком не найдено.")
    else:
        print(f"Успешно удалено {deleted_count} заметок. Остались следующие заметки:")
        display_notes(notes)

def main():

    notes = [
        {'name': 'Алексей', 'title': 'Список покупок', 'description': 'Купить продукты на неделю'},
        {'name': 'Мария', 'title': 'Учеба', 'description': 'Подготовиться к экзамену'}
    ]

    display_notes(notes)
    criterion = input("Введите имя пользователя или заголовок для удаления заметки: ")
    delete_notes(notes, criterion)

if __name__ == "__main__":
    main()

