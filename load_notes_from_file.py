
def load_notes_from_file(filename):
    notes = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            note = {}
            for line in file:
                line = line.strip()
                if line == '---':
                    if note:
                        notes.append(note)
                        note = {}
                else:
                    key, value = line.split(': ', 1)

                    key = key.replace(
                        'Имя пользователя', 'user_name').replace(
                        'Заголовок', 'title').replace(
                        'Описание заметки', 'content').replace(
                        'Статус заметки', 'status').replace(
                        'Дата создания заметки', 'formatted').replace(
                        'Истечение заметки', 'issue_date')

                    note[key] = value.strip()
            if note:
                notes.append(note)

    except FileNotFoundError:
        print(f"Ошибка файл '{filename}' не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {str(e)}")
    return notes

filename = 'filename.txt'
notes = load_notes_from_file(filename)
print(notes)