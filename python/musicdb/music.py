#run with python music.py "artist name in quotes"
#check with:
    # select * from artist
    # left join album on album.artist_id=artist.id
    # left join track on track.album_id=album.id

import json
import pycurl
import StringIO
import urllib
import mysql.connector
import sys

dbUser="root"
dbPass="helix"
dbHost="127.0.0.1"
dbName="music"
#I am using this API:
#http://www.theaudiodb.com/forum/viewtopic.php?t=7

def getAlbums(artistName):
    url = "http://www.theaudiodb.com/api/v1/json/1/searchalbum.php?s=%s"%urllib.quote_plus(artistName)
    print url
    response = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEFUNCTION, response.write)
    c.setopt(c.HTTPHEADER, ['Content-Type: application/json','Accept-Charset: UTF-8'])
    # c.setopt(c.HTTPHEADER, ['Content-Type: application/json'])
    c.setopt(c.POSTFIELDS, '@request.json')
    c.perform()
    c.close()
    albums = json.loads(response.getvalue())
    # albums = _byteify(json.load(response.getvalue(), object_hook=_byteify),ignore_dicts=True)
    response.close()
    return albums

def getTracks(idAlbum):
    url = "http://www.theaudiodb.com/api/v1/json/1/track.php?m=%s"%idAlbum
    response = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEFUNCTION, response.write)
    c.setopt(c.HTTPHEADER, ['Content-Type: application/json','Accept-Charset: UTF-8'])
    # c.setopt(c.HTTPHEADER, ['Content-Type: application/json'])
    c.setopt(c.POSTFIELDS, '@request.json')
    c.perform()
    c.close()
    tracks = json.loads(response.getvalue())
    return tracks

class Database(object):
    @staticmethod
    def getConnection():
        return mysql.connector.connect(user=dbUser,password=dbPass,host=dbHost,database=dbName)
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

class Artist(object):
    def __init__(self,id=0):
        self.name=""

        if(not type(id)==int):
            id=int(id)
        query = "SELECT id,name FROM artist where id=%d " %  id
        result_set = Database.getResult(query,True)
        self.id=id
        if not result_set is None:
            self.id = result_set[0]
            self.content=result_set[1]
        return
    def save(self):
        if self.id>0:
            return self.update()
        else:
            return self.insert()
    def insert(self):
        query = "insert into artist (name) values ('%s')"%(Database.escape(self.name))
        self.id=Database.doQuery(query)
        return self.id
    def update(self):
        query = "update artist set name='%s' where id=%d"%(Database.escape(self.name),self.id)
        # query = ("delete from page where id=%s" % id)
        return Database.doQuery(query)

class Album(object):
    def __init__(self,id=0):
        self.name=""
        self.artist_id=0

        if(not type(id)==int):
            id=int(id)
        query = "SELECT id,name,artist_id FROM album where id=%d " %  id
        result_set = Database.getResult(query,True)
        self.id=id
        if not result_set is None:
            self.id = result_set[0]
            self.content=result_set[1]
            self.artist_id=result_set[2]
        return
    def save(self):
        if self.id>0:
            return self.update()
        else:
            return self.insert()
    def insert(self):
        query = "insert into album (name,artist_id) values ('%s',%d)"%(Database.escape(self.name),self.artist_id)
        self.id=Database.doQuery(query)
        return self.id
    def update(self):
        query = "update album set name='%s',artist_id=%d where id=%d"%(Database.escape(self.name),self.artist_id,self.id)
        # query = ("delete from page where id=%s" % id)
        return Database.doQuery(query)

class Track(object):
    def __init__(self,id=0):
        self.name=""
        self.album_id=0

        if(not type(id)==int):
            id=int(id)
        query = "SELECT id,name,album_id FROM track where id=%d " %  id
        result_set = Database.getResult(query,True)
        self.id=id
        if not result_set is None:
            self.id = result_set[0]
            self.content=result_set[1]
            self.album_id=result_set[2]
        return
    def save(self):
        if self.id>0:
            return self.update()
        else:
            return self.insert()
    def insert(self):
        query = "insert into track (name,album_id) values ('%s',%d)"%(Database.escape(self.name),self.album_id)
        self.id=Database.doQuery(query)
        return self.id
    def update(self):
        query = "update track set name='%s',album_id=%d where id=%d"%(Database.escape(self.name),self.album_id,self.id)
        # query = ("delete from page where id=%s" % id)
        return Database.doQuery(query)

artistName=sys.argv[1]

albums = getAlbums(artistName)
# print type(albums)
# print albums.encode('utf8')
artist = Artist()
artist.name=artistName
artist.save()
for album in albums["album"]:
    # print type(album)
    # print album
    print "..................." + album["strAlbum"] + "................"
    print album["intYearReleased"]
    print album["idAlbum"]
    a = Album()
    a.name=album["strAlbum"]
    a.artist_id=artist.id
    a.save()
    idAlbum = album["idAlbum"]
    tracks = getTracks(idAlbum)
    for track in tracks["track"]:
        print track["strTrack"]
        t = Track()
        t.name=track["strTrack"]
        t.album_id=a.id
        t.save()
