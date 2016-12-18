from flask import Flask, render_template
from random import *

app = Flask('MyApp')

@app.route("/")
def hello():
    return "<h1>hello</h1>"

@app.route("/students")
def students():
    s="My string from the app"
    l=["i am even","i am odd"]
    i=randint(1,100)

    return render_template("students.html",s=s,l=l,i=i)

if __name__=="__main__":
    app.run(debug=True)
