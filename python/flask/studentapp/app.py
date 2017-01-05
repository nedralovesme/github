from flask import Flask,render_template, request,redirect
from student import *
import config,os

#make sure everything is in utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask("MyApp")

@app.route("/test")
def test(methods=["GET"]):
    html = "DBTYPE:%s<br />"%config.DBTYPE
    html += "DBHOST:%s<br />"%config.DBHOST
    html += "DBUSER:%s<br />"%config.DBUSER
    html += "DBNAME:%s<br />"%config.DBNAME
    html += "DBPASS:%s<br />"%config.DBPASS

    # return html

    s = Student(1)
    return s.name

@app.route("/",methods=["GET"])
def home():
    list = Student.getObjects()
    return render_template("students.html",student_list=list,title="Student List")

@app.route("/new_student")
def new_student():
    return  render_template("new_student.html",student=Student())

@app.route("/new_student_submit",methods=["POST","GET"])
def new_student_submit():
    id=request.form.get('id')
    student = Student()
    student.name=request.form.get('name')
    student.save()
    return redirect("/")

@app.route("/update_student",methods=["POST","GET"])
def update_student():
    id=request.args.get('id')
    student = Student(id)
    return  render_template("update_student.html",student=student)

@app.route("/update_student_submit",methods=["POST"])
def update_student_submit():
    id=request.form.get('id')
    student = Student(id)
    student.name=request.form.get('name')
    student.save()
    return redirect("/")

@app.route("/delete_student",methods=["GET"])
def delete_student():
    id=request.args.get('id')
    student = Student(id)
    student.delete()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
