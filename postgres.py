import psycopg2

# information from pg properties
conn = psycopg2.connect(dbname='persons', user='postgres', password='password', host='localhost')

cur = conn.cursor()
# creating DB, table, columns
# cur.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT, skills VARCHAR);")

# adding data to columns
# cur.execute("INSERT INTO users (name) VALUES(%s)", ("Mary",))

# SELECT data from table
cur.execute("SELECT * FROM users")

# update date to columns
# cur.execute("UPDATE users SET skills=(%s) WHERE id=6", ("officiant",))

# output of table
print(cur.fetchall())
conn.commit()
cur.close()
conn.close()
