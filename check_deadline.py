
import datetime

def get_current_date():

    """ Получает текущую дату. """

    return datetime.datetime.now().date()

def parse_date(input_date):

# Преобразует строку в формате 'день.месяц.год' в объект datetime.date.

    return datetime.datetime.strptime(input_date, "%d.%m.%Y").date()

def calculate_days_difference(issue_date):

# Рассчитывает разницу в днях между текущей датой и дедлайном.

    current_date = get_current_date()
    delta = issue_date - current_date
    return delta.days
def process_deadline():

# Основная функция для обработки дедлайна и вывода соответствующих сообщений.

    print(f"Текущая дата: {get_current_date().strftime('%d.%m.%Y')}")
    while True:
        try:
            issue_date_input = input("Введите дату дедлайна (в формате день.месяц.год): ")
            issue_date = parse_date(issue_date_input)
            break
        except ValueError:
            print("Некорректный формат даты. Пожалуйста, убедитесь, что вы вводите дату в формате день.месяц.год.")
    days_difference = calculate_days_difference(issue_date)
    if days_difference < 0:
        print(f"Внимание! Дедлайн истёк {-days_difference} дня(ей) назад.")
    elif days_difference > 0:
        print(f"До дедлайна осталось {days_difference} дня(ей).")
    else:
        print("Дедлайн сегодня!")
if __name__ == "__main__":
    process_deadline()

