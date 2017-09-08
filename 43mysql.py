import pymysql
db = pymysql.connect('localhost', 'root', '', 'test')
cursor = db.cursor()
cursor.execute("SELECT * FROM test")
data = cursor.fetchall()
print(data)
db.close()
