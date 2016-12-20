from flask import Flask,render_template, request,redirect
from objects import *
import mysql.connector
import config


app = Flask("MyApp")

@app.route("/<page_title>")
def home(page_title):
    p = Page(0,page_title)
    return render_template("page.html",page=p)

@app.route("/update")
def update():
    p = Page(1)
    p.title="new title"
    p.author="new author"
    p.content="new content"
    p.save()
    return "i saved"

if __name__=="__main__":
    app.run(debug=True)
