from flask import Flask
import mysql.connector

app = Flask("MyApp")

conn = mysql.connector.connect(
         user='root',
         password='helix',
         host='127.0.0.1',
         database='demo')

cur = conn.cursor()

@app.route("/")
def home():
    query = ("SELECT id,name FROM student")

    cur.execute(query)
    html = "<ul>"
    for (id, name) in cur:
        html += "<li>%s - %s</li>" % (id,name)
    html += "</ul>"
    return html

if __name__=="__main__":
    app.run(debug=True)

cur.close()
conn.close()
