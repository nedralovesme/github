import pg
db=pg.DB(host="localhost", user="postgres", passwd="helix", dbname="demo")
db.debug = True
whatever=db.query("select * from album")
result_list = whatever.namedresult()
# db.insert('album','name'='another album',artist_id=3)
db.update('album',{'name':'updated','id':19})
for result in result_list:
    print "album name is %s artist_id is %d" % (result.name,result.artist_id)
