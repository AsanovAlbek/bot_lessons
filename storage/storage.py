import json

def get_all_groups() -> dict[str, list[str]]:
    try:
        with open('storage/students.json', "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except Exception as e:
        print("Ошибка при чтении файла:", e)
        return {}

def get_tacos_menu() -> list[dict]:
    try:
        with open('storage/tacos_menu.json', "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except Exception as e:
        print("Ошибка при чтении файла:", e)
        return []
