import sqlite3


def run_a_querry(number = int):
    connection = sqlite3.connect('study.db')
    cursor = connection.cursor()
    with open(f'querry_{number}.sql', 'r') as file:
        query_content = file.read()
    sql = query_content
    cursor.execute(sql)
    rows = cursor.fetchall()
    print('Результаты запроса:')
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
