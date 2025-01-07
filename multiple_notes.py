
def block_note():

# Функция создания новой заметки.

    user_name = input('Введите имя пользователя: ')
    title = input('Введите заголовок заметки: ')
    content  = input('Введите описание заметки: ')
    status = input('Введите статус заметки (например "Активна", "Выполнена"): ')
    created_date = input('Введите дату создания заметки в формате "день.месяц.год": ')
    issue_date = input('Введите дату истечения заметки в формате "день.месяц.год": ')
    note = {
        'Имя пользователя': user_name,
        'Заголовок заметки': title,
        'Описание заметки': content,
        'Статус заметки': status,
        'Дата создания заметки': created_date,
        'Дата истечения заметки': issue_date
    }
    return note

def display_notes(notes):

# Функция для отображения всех заметок

    print('Список заметок:')
    for index, note in enumerate(notes, start=1):
        print(f"{index}. Имя пользователя: {note['Имя пользователя']}")
        print(f"  Заголовок заметки: {note['Заголовок заметки']}")
        print(f"  Описание заметки: {note['Описание заметки']}")
        print(f"  Статус заметки: {note['Статус заметки']}")
        print(f"  Дата создания заметки: {note['Дата создания заметки']}")
        print(f"  Дата истечения заметки: {note['Дата истечения заметки']}\n")

def main():
    notes = []
    while True:
        print("Добро пожаловать в менеджер заметок! Вы можетее добавить новую заметку.")
        note = block_note()
        notes.append(note)
        another = input("хотите добавить новую заметку? (да/нет): ")
        if another.lower() != 'да':
            break
    display_notes(notes)
if __name__ == '__main__':
    main()