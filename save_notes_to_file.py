import datetime

dt = datetime.datetime.now()
created_date = dt.strftime('%d.%m.%Y')

def save_notes_to_file():
    
    my_file = open('filename.txt', 'w+', encoding='utf-8')
    user_name = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status = input("Введите статус заметки (Новая, Активна, Завершена): ")
    issue_date = input("Введите дату истечения заметки (день.месяц.год): ")

    my_file.write(f"Имя пользователя: {user_name}\n")
    my_file.write(f"Заголовок: {title}\n")
    my_file.write(f"Описание заметки: {content}\n")
    my_file.write(f"Статус заметки: {status}\n")
    my_file.write(f"Дата создания заметки: {created_date}\n")
    my_file.write(f"Истечение заметки: {issue_date}\n")
    my_file.close()

save_notes_to_file()