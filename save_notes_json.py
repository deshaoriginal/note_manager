import json


def save_notes_json(notes,filename):

        with open('notes.json', 'a', encoding='utf-8') as file:
                json.dump(notes, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    new_notes = ({
        "user_name": "Денис",
        "title": "продукты",
        "content": "купить продукты на неделю",
        "status": "новая",
        "created_date": "20.1.2025",
        "issue_date": "23.1.2025"
    },
    {
        "user_name": "Мария",
        "title": "План работы",
        "content": "Подготовить отчёт",
        "status": "в процессе",
        "created_date": "27.11.2024",
        "issue_date": "28.11.2024"

    })
    save_notes_json(new_notes, 'notes.json')