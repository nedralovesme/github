import config
import mysql.connector

class Friend():
	def __init__ (self, id=0):
		if (not type(id)==int):
			id=int(id)
		conn = Database.getConnection()
		print "got conn"
		cur = conn.cursor()
		print "got cur"
		query = "SELECT id,name FROM student where id=%d" % id
		cur.execute(query)
		result_set = cur.fetchone()
		self.id=id
		if not result_set is None:
			self.name=result_set[1]

		cur.close()
		conn.close()

	def save(self):
		if self.id>0:
			return self.update()
		else:
			return self.insert()

	def insert(self):
		conn = Database.getConnection()
		cur = conn.cursor()
		query = ("insert into pb1 (name,website,email,about) values ('%s','%s','%s', '%s')" % (Database.escape(self.name),website,email,about))
		cur.execute(query)
		conn.commit()
		self.id=cur.lastrowid
		conn.close()
		return self.id

	def update(self):
		conn = Database.getConnection()
		cur = conn.cursor()
		query = "update friend set name='%s' where id=%d"%(Database.escape(self.name),self.id)
		cur.execute(query)
		conn.commit()
		conn.close()
		return self.id

	def delete(self):
		conn = Database.getConnection()
		cur = conn.cursor()
		query = ("update friend set deleted=1 where id = %d" % self.id)
		# query = ("delete from student where id=%s" % id)
		cur.execute(query)
		conn.commit()
		conn.close()
		return True

	def __str__(self):
		return self.name



	@staticmethod
	def getObjects():
		conn = Database.getConnection()
		cur = conn.cursor()
		query = "SELECT id FROM pb1 where deleted=0"
		cur.execute(query)
		result_set = cur.fetchone()
		friends=[]
		for item in result_set:
			id = int(item[0])
			friend.append(Friend(id))
			conn.close()
		return friends


class Database(object):
	@staticmethod
	def getConnection():
		return mysql.connector.connect(user=config.dbUser,password=config.dbPass,host=config.dbHost,database=config.dbName)

	@staticmethod
	def escape(value):
		return value.replace("'","''")
