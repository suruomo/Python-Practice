# 数据库基本操作
import pymysql
conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='suruomo',db='demo')
cur=conn.cursor()
# 查询行数
rows=cur.execute('select * from sys_log')
print(rows)
# 打印表中的多少数据
info = cur.fetchmany(rows)
for ii in info:
    print (ii)
# 关闭游标
cur.close()
# 提交操作，删除插入修改必须
conn.commit()
# 关闭数据库连接
conn.close()