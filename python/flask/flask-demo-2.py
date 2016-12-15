from flask import Flask,render_template
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

    list = cur.fetchall()
    # print list
    return render_template(
        'students.html',
        title='Students',
        student_list=list
    )


if __name__=="__main__":
    app.run(debug=True)

cur.close()
conn.close()
