import mysql.connector
import pg
import config

class Student:
    def __init__(self,id=0):
        self.name=""
        if(not type(id)==int):
            id=int(id)
        query = "SELECT id,name FROM student where id=%d"%id
        result_set = Database.getResult(query,True)
        print "result in constructor",result_set
        print "len(result_set)",len(result_set)
        self.id=id
        if not result_set is None and len(result_set)>1:
            self.name=result_set[1]
            print "self.name",self.name
        return
    def save(self):
        if self.id>0:
            return self.update()
        else:
            return self.insert()
    def insert(self):
        query = ("insert into student (name) values ('%s')"%Database.escape(self.name))
        if config.DBTYPE=="postgresql":
            query+=" returning id"
        self.id=Database.doQuery(query)

        return self.id
    def update(self):
        query = "update student set name='%s' where id=%d"%(Database.escape(self.name),self.id)
        if config.DBTYPE=="postgresql":
            query+=" returning id"
        # query = ("delete from student where id=%s" % id)
        return Database.doQuery(query)
    def delete(self):
        query = ("delete from student where id=%d"%self.id)
        Database.doQuery(query)
        return True
    def __str__(self):
     return self.name
    @staticmethod
    def getObjects():
        query = "SELECT id FROM student"
        result_set = Database.getResult(query)
        students=[]
        print result_set
        for item in result_set:
            print "item:",item
            id = int(item[0])
            print "id:",id
            students.append(Student(id))
        return students

class Database(object):
    @staticmethod
    def getConnection():

        if config.DBTYPE=="mysql":
            return mysql.connector.connect(user=config.DBUSER,password=config.DBPASS,host=config.DBHOST,database=config.DBNAME)
        if config.DBTYPE=="postgresql":
            return pg.DB(host=config.DBHOST, user=config.DBUSER, passwd=config.DBPASS, dbname=config.DBNAME)
    @staticmethod
    def escape(value):
        return value.replace("'","''")
    @staticmethod
    def getResult(query,getOne=False):
        """Return a tuple of results or a single item (not in a tuple)
        """
        result_set=()
        conn = Database.getConnection()
        if config.DBTYPE=="mysql":
            cur = conn.cursor()
            cur.execute(query)
            if getOne:
                result_set = cur.fetchone()
            else:
                result_set = cur.fetchall()
            cur.close()
        if config.DBTYPE=="postgresql":
            result = conn.query(query)
            result_set=result.getresult()
            if getOne and result_set:
                result_set=result_set[0]
        conn.close()
        return result_set
    @staticmethod
    def doQuery(query):
        conn = Database.getConnection()
        if config.DBTYPE=="mysql":
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            lastId = cur.lastrowid
            cur.close()
        if config.DBTYPE=="postgresql":
            result = conn.query(query)
            # print result
            # tmp = result.getresult()
            # print tmp
            # print tmp[0][0]
            lastId = result.getresult()[0][0]
            print "lastId=%d"%lastId
        conn.close()
        return lastId
