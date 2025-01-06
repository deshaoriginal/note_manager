# Отображаем текущий статус заметки
from random import choice


def dispaly_current_status(status):
    print(f'Текущий статус заметки: \'{status}\'')

# Запрашиваем у пользователя новый статус заметки

def get_new_status():
    status_options = {
        1: "выполнено",
        2: "в процессе",
        3: "отложено"
    }

    while True:
        print("\nВыберите новый статус заметки:")
        for key,value in status_options.items():
            print(f"{key}, {value}")
        choice = input("Ваш выбор: ")
        try:
            choice = int(choice)
            if choice in status_options:
                return status_options[choice]
            else:
                print("Ошибка: выберите корректный номер статуса.")
        except ValueError:
            print("Ошибка: введите числовое значение.")

# Основная функция программы для обновления статуса заметки.

def update_note_status():
    current_status = "в процессе" # Пример начального статуса заметки
    dispaly_current_status(current_status)
    new_status = get_new_status()
    current_status = new_status
    print(f"Статус заметки успешно обновлен на: \"{current_status}\"")
if __name__ == "__main__":
    update_note_status()