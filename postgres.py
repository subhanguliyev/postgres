# information from pg admin properties
DB_NAME = 'persons'
DB_HOST = 'localhost'
DB_USER = 'postgres'
DB_PASS = 'password'

import psycopg2

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

cur = conn.cursor()

# cur.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT, skills VARCHAR);")

# cur.execute("INSERT INTO users (name) VALUES(%s)", ("Mary",))

cur.execute("SELECT * FROM users")

# cur.execute("UPDATE users SET skills=(%s) WHERE id=6", ("officiant",))

print(cur.fetchall())
conn.commit()
cur.close()
conn.close()
