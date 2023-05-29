# decryption
def dec(rx):
    rx1=rx[4:len(rx)-4]
    
    rx2=''
    rx3=''
    for i in rx1:
        if i in '#!':
            continue
        else:
            rx2+=i
    for i in range(0,len(rx2),2):
        rx3+=chr(ord(rx2[i])-1)
    return rx3



# encryption
def enc(rx):
    
    rx1='`1cd'
    for i in range(0,len(rx)):
        c=rx[i]
        rx1+=chr(ord(c)+1)+chr(ord(c)-1)+'#!'

    return rx1+'0cd`'


# customer id

def csid(n):
    
    import mysql.connector as mysql

    mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
    cursor=mycon.cursor()
    cursor.execute("select cus_id from cus_info where cus_name='{}'".format(n))
    data=cursor.fetchall()
    try:
        return data[0][0]
    except:
        return None
    

    

