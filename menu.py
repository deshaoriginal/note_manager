def create_note():
    print("Новая заметка создана!")

def display_note():
    print("Отображение всех заметок.")

def update_note():
    print("Обновление заметки.")

def delete_note():
    print("Заметка удалена.")

def search_notes():
    print("Поиск заметок.")

def main_menu():
    while True:

        print("""
        
Меню действий:

1. Создать новую заметку
2. Показать все заметки
3. Обновить заметку
4. Удалить заметку
5. Найти заметку
6. Выйти из программы
""")

        choice = input("Ваш выбор: ")
        if choice == '1':
            create_note()
        elif choice == '2':
            display_note()
        elif choice == '3':
            update_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            search_notes()
        elif choice == '6':
            print("Программа завершена. Спасибо за использование!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")

if __name__ == '__main__':
    main_menu()