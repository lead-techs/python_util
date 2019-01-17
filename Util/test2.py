import pymysql#导入pymysql模块
conn = pymysql.Connect(host='localhost',port=3306,user='root',passwd='root',db='cms',charset='utf8')
cur=conn.cursor()#获取一个游标
sql_select = "select * from emp"#定义查询
cur.execute(sql_select) #执行查询
print(sql_select)
data =cur.fetchall() #获取查询到数据
#cur.fetchone()获取一条数据
for i in range(len(data)):
    print(data[i])
conn.commit()#提交事务
cur.close()#关闭游标
conn.close()#释放数据库资源