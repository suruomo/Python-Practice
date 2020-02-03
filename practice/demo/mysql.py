import pymysql
#打开数据库连接
conn = pymysql.connect('localhost',user = "root",passwd = "suruomo",db = "demo")
print (conn)
print (type(conn))