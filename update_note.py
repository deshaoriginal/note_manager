import datetime
from dataclasses import field


def validate_date(date_str):

# Проверка строки на правильный формат даты

    try:
        datetime.datetime.strptime(date_str, '%d.%m.%Y')
        return True
    except ValueError:
        return False

def update_note(note):

# Функция обновления заметки

    print("Текущие данные заметки:")
    print(note)
    fields = ['user_name', 'title', 'content', 'status', 'issue_date']
    while True:
        field = input(f"какие данные на выходе обновить? ({', '.join(fields)}): ")
        if field in fields:
            if field == 'issue_date':
                new_value = input("Введите новую дату (дд.мм.гггг): ")
                if validate_date(new_value):
                    note[field] = new_value
                    break
                else:
                    print("Неверный формат даты. Пожалуйста, используйте формат дд.мм.гггг.")
            else:
               new_value = input(f"Введите новое значение для {field}: ")
               note[field] = new_value
               break
        else:
            print("Ошибка: Некорректное имя поля. Попробуйте еще раз.")
    print("Заметка обновлена:")
    print(note)
    return note

# Пример использования функции

example_note = {
    'user_name': 'Алексей',
    'title': 'Список покупок',
    'content': 'Купить продукты на неделю',
    'status': 'новая',
    'created_date': '27.11.2024',
    'issue_date': '30.11.2024'
}
update_note = update_note(example_note)