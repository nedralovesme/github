import mysql.connector
import config

class Student:
    def __init__(self,id=0):
        if(not type(id)==int):
            id=int(id)
        query = "SELECT id,name FROM student where id=%d"%id
        result_set = Database.getResult(query,True)
        self.id=id
        if not result_set is None:
            self.name=result_set[1]
        return
    def save(self):
        if self.id>0:
            return self.update()
        else:
            return self.insert()
    def insert(self):
        query = ("insert into student (name) values (\"%s\")"%Database.escape(self.name))
        self.id=Database.doQuery(query)
        return self.id
    def update(self):
        query = "update student set name='%s' where id=%d"%(Database.escape(self.name),self.id)
        # query = ("delete from student where id=%s" % id)
        return Database.doQuery(query)
    def delete(self):
        query = ("update student set deleted=1 where id=%d"%self.id)
        Database.doQuery(query)
        return True
    def __str__(self):
     return self.name
    @staticmethod
    def getObjects():
        query = "SELECT id FROM student where deleted=0"
        result_set = Database.getResult(query)
        students=[]
        for item in result_set:
            id = int(item[0])
            students.append(Student(id))
        return students

class Database(object):
    @staticmethod
    def getConnection():
        return mysql.connector.connect(user=config.dbUser,password=config.dbPass,host=config.dbHost,database=config.dbName)
    @staticmethod
    def escape(value):
        return value.replace("'","''")
    @staticmethod
    def getResult(query,getOne=False):
        conn = Database.getConnection()
        cur = conn.cursor()
        cur.execute(query)
        if getOne:
            result_set = cur.fetchone()
        else:
            result_set = cur.fetchall()
        cur.close()
        conn.close()
        return result_set
    @staticmethod
    def doQuery(query):
        conn = Database.getConnection()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        lastId = cur.lastrowid
        cur.close()
        conn.close()
        return lastId
