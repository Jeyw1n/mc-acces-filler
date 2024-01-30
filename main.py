import pyodbc
# import g4f
import os

from data_manager import get_settings
from fields_generator import func_dict


SETTINGS = get_settings()


def fill_table() -> list:
    """Создание таблицы с данными"""

    data: list = []

    for i in range(SETTINGS['lines_count']):
        gen_functions = func_dict()
        if SETTINGS['has_id']:
            data.append([i + 1] + [gen_functions[field]() for field in SETTINGS['fields']])
        else:
            data.append([gen_functions[field]() for field in SETTINGS['fields']])

    return data


def main() -> None:
    try:
        # Устанавливаем абсолютный путь, если SETTINGS['abs_path'] == False.
        file_path: str = SETTINGS['file_path']
        if not SETTINGS['abs_path']:
            file_path = os.path.abspath(SETTINGS['file_path'])

        # Connect database.
        con_string: str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' fr'DBQ={file_path};'
        conn = pyodbc.connect(con_string)
        cursor = conn.cursor()

        print(f"База данных [{SETTINGS['file_path']}] была подключена.")

        # Fill '?, '
        if SETTINGS['has_id']:
            fields_count = '?, ' + ', '.join(["?" for i in SETTINGS['fields']])
        else:
            fields_count = ', '.join(["?" for i in SETTINGS['fields']])

        cursor.executemany(f'INSERT INTO {SETTINGS["table"]} VALUES ({fields_count})', fill_table())
        conn.commit()

        print(f"Таблица [{SETTINGS['table']}] заполнена успешно!")

    except pyodbc.Error as e:
        print("Ошибка:", e)


# def send_prompt():
#     val_name = ''
#     response = g4f.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": f""}],
#         stream=True,
#     )
#     for message in response:
#         print(message, flush=True, end='')


if __name__ == '__main__':
    send_prompt()
