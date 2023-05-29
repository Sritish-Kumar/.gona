
import mysql.connector as mysql
import os,random,time
mycon=mysql.connect(host="localhost",user="root",passwd="root",database=" ")
if mycon.is_connected():
    pass
else:
    print("\tError connecting to database\n")
    print('\t - inform the seller -\n')

print()
print('\t set up started\n')
cursor=mycon.cursor()
cursor.execute("create database gona")
cursor.execute("use gona")
cursor.execute("create table airp(product_id char(20) primary key,name varchar(100),price int)")
import csv
#TABLE 1
f1=open(r"csv files\airpurip.csv","r")
fa=csv.reader(f1)
for i in fa:
    cursor.execute("insert into airp values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 2
cursor.execute("create table ceramic(product_id char(20) primary key,name varchar(100),price int)")
f2=open(r"csv files\ceramic.csv","r")
fce=csv.reader(f2)
for i in fce:
    cursor.execute("insert into ceramic values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 3
cursor.execute("create table concrete(product_id char(20) primary key,name varchar(100),price int)")
f3=open(r"csv files\concrete.csv","r")
fco=csv.reader(f3)
for i in fco:
    cursor.execute("insert into concrete values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 4
cursor.execute("create table cutting(product_id char(20) primary key,name varchar(100),price int)")
f4=open(r"csv files\cutting.csv","r")
fcu=csv.reader(f4)
for i in fcu:
    cursor.execute("insert into cutting values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 5
cursor.execute("create table digging(product_id char(20) primary key,name varchar(100),price int)")
f5=open(r"csv files\digging.csv","r")
fdi=csv.reader(f5)
for i in fdi:
    cursor.execute("insert into digging values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 6
cursor.execute("create table flop(product_id char(20) primary key,name varchar(100),price int)")
f6=open(r"csv files\floweringp.csv","r")
ffl=csv.reader(f6)
for i in ffl:
    cursor.execute("insert into flop values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 7        
cursor.execute("create table folp(product_id char(20) primary key,name varchar(100),price int)")
f7=open(r"csv files\foliage.csv","r")
ffo=csv.reader(f7)
for i in ffo:
    cursor.execute("insert into folp values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 8
cursor.execute("create table fruit(product_id char(20) primary key,name varchar(100),price int)")
f8=open(r"csv files\fruit.csv","r")
ffr=csv.reader(f8)
for i in ffr:
    cursor.execute("insert into fruit values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 9
cursor.execute("create table grow(product_id char(20) primary key,name varchar(100),price int)")
f9=open(r"csv files\grow.csv","r")
fgr=csv.reader(f9)
for i in fgr:
    cursor.execute("insert into grow values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 10
cursor.execute("create table hand(product_id char(20) primary key,name varchar(100),price int)")
f10=open(r"csv files\hand.csv","r")
fha=csv.reader(f10)
for i in fha:
    cursor.execute("insert into hand values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 11
cursor.execute("create table indp(product_id char(20) primary key,name varchar(100),price int)")
f11=open(r"csv files\indoorp.csv","r")
fin=csv.reader(f11)
for i in fin:
    cursor.execute("insert into indp values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 12
cursor.execute("create table lowp(product_id char(20) primary key,name varchar(100),price int)")
f12=open(r"csv files\lowmain.csv","r")
flo=csv.reader(f12)
for i in flo:
    cursor.execute("insert into lowp values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 13
cursor.execute("create table metallic(product_id char(20) primary key,name varchar(100),price int)")
f13=open(r"csv files\metallic.csv","r")
fme=csv.reader(f13)
for i in fme:
    cursor.execute("insert into metallic values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 14
cursor.execute("create table seedling(product_id char(20) primary key,name varchar(100),price int)")
f14=open(r"csv files\seedling.csv","r")
fse=csv.reader(f14)
for i in fse:
    cursor.execute("insert into seedling values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 15           
cursor.execute("create table vegetable(product_id char(20) primary key,name varchar(100),price int)")
f15=open(r"csv files\vegetables.csv","r")
fve=csv.reader(f15)
for i in fve:
    cursor.execute("insert into vegetable values('{}','{}',{})".format(i[0],i[1],i[2]))
#TABLE 16
cursor.execute("create table watering(product_id char(20) primary key,name varchar(100),price int)")
f16=open(r"csv files\watering.csv","r")
fwa=csv.reader(f16)
for i in fwa:
    cursor.execute("insert into watering values('{}','{}',{})".format(i[0],i[1],i[2]))          
#TABLE 17
cursor.execute("create table cus_cart(cus_id char(10),product_id varchar(10),name varchar(100),price int)")
#TABLE 18
cursor.execute("create table cus_info(cus_id varchar(100) primary key,cus_name varchar(100) unique,cus_pass varchar(100));")
mycon.commit()
cursor.execute("insert into cus_info values('cs1','sritish','1cddb#!mk#!b`#!tr#!tr#!20#!31#!0cd');")
#TABLE 19
cursor.execute("create table cus_profile(cus_id char(10) primary key,address varchar(200),pincode int,emailid varchar(100),phone bigint)")
#TABLE 20
cursor.execute("create table cus_buy(cus_id char(10),product_id varchar(10),name varchar(100),price int)")
#TABLE 21
cursor.execute("create table todayd(product_id char(20) primary key,name varchar(200),price int,discount int)")
mycon.commit()

i=0   ########## loading bar
r=[0,5]
while i<45:
    
    s=random.randint(r[0],r[1])
    if s<i:
        continue
    i=s
    r[0]+=7
    r[1]+=10
    q=i*2
    if q>100:
        q=100
    print('░░'*i)
    print(f'<{q}>')
    time.sleep(1)
    os.system('cls')
print('░░'*i)
print('< 100 >')
print()
print("\t ALL SETUP COMPLETED\n")
mycon.close()