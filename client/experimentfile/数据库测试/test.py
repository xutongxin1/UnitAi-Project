import pymysql

# 打开数据库连接
db = pymysql.connect("192.168.0.3", "account", "019150", "account")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql= "select*from acc where name='xutongxin'"
# 使用 execute()  方法执行 SQL 查询
cursor.execute(sql)

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()

print(data)
for name in data:
    pasd=name[4]
    print(pasd)
# 关闭数据库连接
db.close()