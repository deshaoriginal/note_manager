
import datetime

def current_date(create_date_str):

# Проверка правильной даты

    try:
        return datetime.datetime.strptime(create_date_str, '%d.%m.%Y')
    except ValueError:
        return None

def create_note():

# Функция для создания заметки запрашивает у пользователя данные

    user_name = input('Введите имя пользователя: ')
    title = input('Введите заголовок заметки: ')
    content  = input('Введите описание заметки: ')
    status = input('Введите статус заметки (например, "Новая" "Активна", "Выполнена"): ')
    issue_date_str = input('Введите дату истечения заметки в формате "день.месяц.год": ')
    issue_date = current_date(issue_date_str)

    while issue_date is None:
        print("Неверный формат даты, Пожалуйста, используйте формат (день.месяц.год): ")
        issue_date_str = input("Введите дату истечения заметки (день.месяц.год): ")
        issue_date = current_date(issue_date_str)

    created_date = datetime.datetime.now().strftime('%d.%m.%Y')

    note = {
        'user_name': user_name,
        'title': title,
        'content': content,
        'status': status,
        'created_date': created_date,
        'issue_date': issue_date.strftime('%d.%m.%Y')
    }
    return note

# Основная функция

if __name__ == "__main__":
    note = create_note()
    print("Заметка создана: ", note)
