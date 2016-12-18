import mysql.connector
import config

class Student:
    def __init__(self,id=0):
        if(not type(id)==int):
            id=int(id)
        conn = Database.getConnection()
        cur = conn.cursor()
        query = "SELECT id,name FROM student where id=%d"%id
        cur.execute(query)
        result_set = cur.fetchone()
        print result_set
        self.id=id
        if not result_set is None:
            self.name=result_set[1]

        cur.close()
        conn.close()
        return
    def update(self):
        conn = Database.getConnection()
        cur = conn.cursor()
        query = "update student set name='%s' where id=%d"%(self.name,self.id)
        # query = ("delete from student where id=%s" % id)
        cur.execute(query)
        conn.commit()
        return self.id
    def save(self):
        if self.id>0:
            return self.update()
        else:
            return self.insert()
    def insert(self):
        conn = Database.getConnection()
        cur = conn.cursor()
        query = ("insert into student (name) values (\"%s\")"%self.name)
        # query = ("delete from student where id=%s" % id)
        cur.execute(query)
        conn.commit()
        self.id=cur.lastrowid
        return self.id
    def delete(self):
        conn = Database.getConnection()
        cur = conn.cursor()
        query = ("update student set deleted=1 where id=%d"%self.id)
        # query = ("delete from student where id=%s" % id)
        cur.execute(query)
        conn.commit()
        return True
    def __str__(self):
     return self.name
    @staticmethod
    def getObjects():
        conn = Database.getConnection()
        cur = conn.cursor()
        query = "SELECT id FROM student where deleted=0"
        cur.execute(query)
        result_set = cur.fetchall()
        students=[]
        for item in result_set:
            id = int(item[0])
            students.append(Student(id))
        return students

class Database(object):
    @staticmethod
    def getConnection():
        return mysql.connector.connect(user=config.dbUser,password=config.dbPass,host=config.dbHost,database=config.dbName)
