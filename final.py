# Создаем словарь для хранения информиции о заметке

note = {}

note['user_name'] = input('Введите имя пользователя: ')
note['content'] = input('Введите описание заметки: ')
note['status'] = input('Введите статус заметки (например "Активна", "Выполнена"): ')
note['created_date'] = input('Введите дату создания заметки в формате "день.месяц.год": ')
note['issue_date'] = input('Введите дату истечения заметки в формате "день.месяц.год": ')

# Добавляем заголовки в список внутри словоря

note['titles'] = []
for i in range(3):
    title = input(f'Введите заголовок заметки {i + 1}: ')
    note['titles'].append(title)

#Выводим собранные данные

print('\nСобранные данные о заметке:')
for key, value in note.items():
    print(f'{key.capitalize()}, {value}')