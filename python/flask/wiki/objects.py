import mysql.connector
import config
from time import strftime

class Page:

    def __init__(self,id=0,title=""):
        self.content=""
        self.title=""
        self.mdate=strftime("%Y-%m-%d %H:%M:%S")
        self.author=""

        if(not type(id)==int):
            id=int(id)
        whereClause = "id=%d"%id

        if len(title)>0:
            whereClause = "title='%s'"%title

        query = "SELECT id,content,title,mdate,author FROM page where %s " %  whereClause
        result_set = Database.getResult(query,True)
        self.id=id
        if not result_set is None:
            self.id = result_set[0]
            self.content=result_set[1]
            self.title=result_set[2]
            self.mdate=result_set[3]
            self.author=result_set[4]
        return
    def save(self):
        if self.id>0:
            return self.update()
        else:
            return self.insert()
    def insert(self):
        query = "insert into page (title,content,author,mdate) values ('%s','%s','%s','%s')"%(Database.escape(self.title),Database.escape(self.content),Database.escape(self.author),Database.escape(self.mdate))
        self.id=Database.doQuery(query)
        return self.id
    def update(self):
        query = "update page set title='%s',content='%s',author='%s',mdate='%s' where id=%d"%(Database.escape(self.title),Database.escape(self.content),Database.escape(self.author),strftime("%Y-%m-%d %H:%M:%S"),self.id)
        # query = ("delete from page where id=%s" % id)
        return Database.doQuery(query)
    def delete(self):
        query = ("delete from page where id=%d"%self.id)
        Database.doQuery(query)
        return True
    def __str__(self):
     return self.title
    @staticmethod
    def getObjects():
        query = "SELECT id FROM page"
        result_set = Database.getResult(query)
        pages=[]
        for item in result_set:
            id = int(item[0])
            pages.append(Page(id))
        return pages

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
