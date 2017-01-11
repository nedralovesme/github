from flask import Flask,render_template, request, redirect, url_for
from student import *
import config,os

#make sure everything is in utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def debug(line):
	import time
	target = open("debug.log", "w")
	ip=request.remote_addr

	timestamp =  time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	target.write("\n[%s][%s] %s"%(timestamp,ip, line))
	target.close()


app = Flask("MyApp")

@app.route("/test")
def test(methods=["GET"]):
    html = "DBTYPE:%s<br />"%config.DBTYPE
    html += "DBHOST:%s<br />"%config.DBHOST
    html += "DBUSER:%s<br />"%config.DBUSER
    html += "DBNAME:%s<br />"%config.DBNAME
    html += "DBPASS:%s<br />"%config.DBPASS
    debug("test")
    debug("test")
    debug("test")
    # return html

    s = Student(1)
    return render_template("layout.html")
    # return s.name

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

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__=="__main__":
    app.run(debug=True)
