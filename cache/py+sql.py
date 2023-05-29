import mysql.connector as mysql

mycon=mysql.connect(host='localhost',user='root',passwd='root',database='12cs')

if mycon.is_connected():
    print('sucessfool')
else:
    print('error')

cursor=mycon.cursor()

cursor.execute('show tables;')
data=cursor.fetchall()
print(data)
print(type(data))
for i in data:
    print(i)
print()


cursor.execute("insert into emp values(5,'laman',60000);")
cursor.execute('select * from emp;')
data=cursor.fetchall()
print(cursor.rowcount)
for i in data:
    print(i)
print()

cursor.execute('select * from dept')
print(cursor.rowcount)
data=cursor.fetchall()
for i in data:
    print(i)
mycon.close()
