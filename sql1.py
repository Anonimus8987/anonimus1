import sqlite3

connection = sqlite3.connect('my_sql.db')

sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS my_sql (user_id INTEGER, username TEXT);')

sql.execute('INSERT INTO my_sql (user_id, username) VALUES (0, "pav_ok");')

print(sql.execute('SELECT user_id, username FROM my_sql;').fetchall())

print(sql.execute('SELECT * FROM my_sql WHERE user_id=1').fetchone())

connection.commit()


