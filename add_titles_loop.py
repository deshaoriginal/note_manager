
# Цикл для добавления заголовков

def main():

    # Создаем пустой список для хранения заголовков

    titles = []
    while True:

        # Запрашиваем у пользователя ввод заголовка или команду для завершения

        title = input("Введите заголовок (или оставьте пустым для завершения): ").strip()

        # Проверяем, не является ли ввод пустой строкой или командой 'стоп' для завершения

        if title == "" or title.lower() == "стоп":
            break

        # Добавляем заголовок в список, если он не пустой

        if title:
            titles.append(title)

    # Выводим список заголовков после завершения ввода

    print("\nЗаголовки заметки:")
    for title in titles:
        print(f"- {title}")
if __name__ == "__main__":
    main()

