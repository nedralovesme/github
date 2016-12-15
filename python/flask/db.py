import mysql.connector

conn = mysql.connector.connect(
         user='root',
         password='helix',
         host='127.0.0.1',
         database='demo')

cur = conn.cursor()

query = ("SELECT id,name FROM student")

cur.execute(query)

for (id, name) in cur:
  print "%s, %s" % (id, name)

cur.close()
conn.close()
