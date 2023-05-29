
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
    
