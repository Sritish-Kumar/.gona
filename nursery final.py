import mysql.connector as mysql,dec,enc,csid,time,random,os

cs_id=None
adminid=[('sritish','class'),('ritesh','class')]
def main():

    def admin():

        def allsold():
            mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
            cursor=mycon.cursor()

            cursor.execute('select * from cus_buy')
            data=cursor.fetchall()
            print()
            for i in data:
                print(i)
            print()
            while True:
                print('\t -> press 0 to go back')
                print('\t -> press 1 to sort by most selling products')
                print('\t -> press 1 to sort by least selling products')
                print()
                inp=input('<.> ').lower().strip()
                if inp in ['0','return','back']:
                    mycon.close()
                    return
                elif inp in ['1','most']:
                    cursor.execute('select product_id,count(*),name,price from cus_buy group by product_id order by count(*) desc')
                    data=cursor.fetchall()
                    for i in data:
                        print(i[0],')',i[2],'->',i[1],'--','Rs.',i[3])
                elif inp in ['2','least']:
                    cursor.execute('select product_id,count(*),name,price from cus_buy group by product_id order by count(*) asc')
                    data=cursor.fetchall()
                    for i in data:
                        print(i[0],')',i[2],'->',i[1],'--','Rs.',i[3])
                else:
                    print('\t !!! INVALID KEY !!!\n')
                    continue


        def cslist():
            mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
            cursor=mycon.cursor()
            cursor.execute('select * from cus_info')
            data=cursor.fetchall()
            print()
            print('\t\t\t - CUSTOMERS - \n')
            for i in data:
                print(i[0],'--',i[1],'--',i[2])
            print()
            while True:
                print()
                print('\t -> press 0 to go back')
                print('\t -> press 1 to sort customer by their number of orders')
                print('\t -> type the customer name/id to view its orders')
                print()
                cs_inp=input('<.>').lower().strip()
                print()
                if cs_inp in ['0','back','return']:
                    mycon.close()
                    return
                elif cs_inp in ['1','sort']:
                    cursor.execute('select cus_buy.cus_id,count(cus_buy.cus_id),cus_info.cus_name from cus_buy,cus_info where cus_info.cus_id=cus_buy.cus_id group by cus_id')
                    data=cursor.fetchall()
                    for i in data:
                        print(i[0],')',i[1],'->',i[2])
                    continue

                elif cs_inp.isalnum():
                    rx=cs_inp
                    if cs_inp.isalpha():

                        rx=csid.csid(cs_inp)
                         
                        if rx==None:

                            print('\t !!! Name not found !!!\n')
                            continue
                    
                    cursor.execute('select name,price from cus_buy where cus_id="{}"'.format(rx))
                    data=cursor.fetchall()
                    for i in data:
                        print(i[0],'->>',i[1])
                    if len(data)==0:
                        print('\t !!! ID NOT FOUND !!!\n')
                        continue
                        
                else:
                    print('\t !!!! INVALID KEY !!!!\n')
                    continue
                              


        def dropt(n,x=None):
            mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
            cursor=mycon.cursor()
            print()
            
            while True:

                cursor.execute('select * from {}'.format(n))
                data=cursor.fetchall()
                for i in data:
                    print(i[0],')',i[1],i[3],'--','[',i[2],']')
                print('\t to go back press"0"\n')
                print("\t if you want to select multiple items then you can write them in between commas','")
                dropt_inp=input('Enter the items you want to drop: ').strip().split(',')
                
                if '0' in dropt_inp:
                    mycon.close()
                    return
                found='neg'
                for i in dropt_inp:

                    if i in ['pots','bag','seedling','seeds','seed','tray','seedling tray','ceramic pot','grow bag','planter','plants','plant','holes','steel','cultivator','rake','pipe']:
                        print()
                        print('\t !!! {} NOT FOUND !!!\n'.format(i))

                        continue
                    if i.isdigit():
                        print()
                        print('\t !!! Enter the correct number !!! ','[',i,']\n')
                        continue
                    elif i.isalpha():
                        try:
                            cursor.execute('select * from {} where name like "%{}%"'.format(n,i))
                            data=cursor.fetchall()

                            cursor.execute('delete from {} where name like "%{}%"'.format(n,i))
                            mycon.commit()
                            
                            if len(data)!=0:
                                found+='pos'
                        except:
                            print()
                            print('\t !!! Enter the Correct Data !!!','[',i,']\n')
                            pass
                        
                    elif i.isalnum():
                        try:
                            cursor.execute('select * from {} where name like "%{}%" or product_id="{}"'.format(n,i,i))
                            data=cursor.fetchall()
                            cursor.execute('delete from {} where name like "%{}%" or product_id="{}"'.format(n,i,i))
                            mycon.commit()
                            if len(data)!=0:
                                found+='pos'
                            
                        except:
                            print()
                            print('\t !!! Enter the Correct Data !!!','[',i,']\n')
                            continue


                if 'pos' in found:
                    break
                else:
                    continue
            print()
            print('\t\t ### sucessfully droped ###\n')
            mycon.close()
            return


        def add(rx,rx1):

            def sub(data,name):
                for i in data:
                    if i[1]==name:
                        return 'exist'

                
            mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
            cursor=mycon.cursor()
            while True:
                
                cursor.execute('select * from {}'.format(rx))
                data1=cursor.fetchall()
                count=cursor.rowcount
                
                
                print('\tpress 0 to return\n')
                while True:
                    name=input('\tEnter the name of the product: ')
                    if name=='0' or name=='return':
                        return
                    x=sub(data1,name)
                    if x=='exist':
                        print('\t !!! PRODUCT ALREADY EXIST !!!\n')
                        continue
                    break
                price=int(input('\tenter the price: '))
                cursor.execute('insert into {} values("{}","{}",{})'.format(rx,rx1+str(count+1),name,price))
                mycon.commit()
                print()
                print('press enter to insert another product')
                chck=input("->").lower().strip()

                if chck in ['',' ','enter']:
                    continue
                break
            return
                


        def addt(n,rx,rx1):
            mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
            cursor=mycon.cursor()
            
            print()
            while True:
                cursor.execute('select * from {}'.format(rx))
                data=cursor.fetchall()
                for i in data:
                    print(i[0],')',i[1],'->',i[2])
                
                
                print('\t - press "0" to go back -\n')
                print("\t if you want to select multiple items then you can write them in between commas','\n")
                inp=input('=>').lower().rstrip().split(',')
                if inp=='0':
                    mycon.close()
                    return
                y=''

                for i in inp:
                    
                        
                    if i.isdigit():
                        try:

                            cursor.execute("select * from {} where product_id='{}'".format(rx,rx1+i))
                            data=cursor.fetchall()
                            print()
                            print(data[0][1],'->',data[0][2])
                            print()
                            dis=input('\t DISCOUNTED MONEY: ')
                            try:
                                cursor.execute("insert into todayd values('{}','{}',{},{})".format(data[0][0],data[0][1],data[0][2],dis))
                                mycon.commit()
                                y+='1'
                            except:
                                print()
                                print('\t !!! DATA ALREADY EXIST !!!\n')
                                continue
                        except:
                            print()
                            print('\t !!! {} NOT FOUND !!! \n'.format(i))
                            y+='0'
                            continue
                        
                    elif i in ['pots','bag','seedling','seeds','seed','tray','seedling tray','ceramic pot','grow bag','planter','plants','plant','holes','steel','cultivator','rake','pipe']:
                        print()
                        print('\t !!! {} NOT FOUND !!! \n'.format(i))
                        y+='0'
                        continue

                    elif i.isalpha():
                        try:
                            cursor.execute("select * from {} where name like '%{}%'".format(rx,i))
                            data=cursor.fetchall()
                            print(data[0][1],'->',data[0][2])
                            dis=input('\t DISCOUNTED MONEY: ')
                            cursor.execute("insert into todayd values('{}','{}',{},{})".format(data[0][0],data[0][1],data[0][2],dis))
                            mycon.commit()
                            y+='1'
                        except:
                            print()
                            print('\t !!! {} NOT FOUND !!! \n'.format(i))
                            y+='0'
                            continue

                       
                    elif i.isalnum():
                        try:
                            cursor.execute("select * from {} where name or product_id like '%{}%'".format(rx,i))
                            data=cursor.fetchall()
                            print(data[0][1],'->',data[0][2])
                            dis=input('\t DISCOUNTED MONEY: ')
                            cursor.execute("insert into todayd values('{}','{}',{},{})".format(data[0][0],data[0][1],data[0][2],dis))
                            
                            mycon.commit()
                            y+='1'
                        except:
                            print()
                            print('\t !!! {} NOT FOUND !!! \n'.format(i))
                            y+='0'
                            continue

                    else:

                        print()
                        print('\t !!! {} NOT FOUND !!! \n'.format(i))
                        y+='0'
                        continue

                if '0' in y:
                    print('\t\t *** {} VALUES NOT FOUND ***'.format(y.count('0')))

                cursor.execute('select * from todayd')
                data=cursor.fetchall()
                print()
                print('='*80)
                for i in data:
                    print(i[0],')',i[1],'->',i[3],'( OFFER PRICE )')
                print('='*80)
                mycon.close()
                return
                
  

        def prin(n):
            print()
            print()
            while True:

                
                print('\n\tTo go back press 0\n')
                print("1) LOW MAINTENANCE PLANTS")
                print("2) FOLIAGE PLANTS")
                print("3) INDOOR PLANTS")
                print("4) AIR PURIFIER PLANTS")
                print("5) FLOWERING")
                print('6) Ceramic Pots')
                print('7) Metallic Pots')
                print('8) Concrete Pots')
                print('9) Seedling Tray')
                print('10) Grow Bags')
                print('11) CUTTING TOOLS')
                print('12) HAND TOOLS')
                print('13) DIGGING TOOLS')
                print('14) WATERING TOOLS')
                print('15) FRUITS SEEDS')
                print('16) VEGETABLE SEEDS')
                print()
                inp=input('enter: ').lower().strip()

                if inp=='0':
                    return
                elif inp in ['1)','1','low maintenance plants','low','low maintenance','low maintenance plant']:
                    rx='lowp'
                    rx1='l'
                elif inp in ['2)','2','foligae plants','foliage plant','foliage']:
                    rx='folp'
                    rx1='f'
                elif inp in ['3)','3','indoor plants','indoor','indoor plant',]:
                    rx='indp'
                    rx1='i'
                elif inp in ['4)','4','air purifier plants','purifier','purifier plant',]:
                    rx='airp'
                    rx1='a'
                elif inp in ['5)','5','flowering plants','flowering','flowering plant',]:
                    rx='flop'
                    rx1='fl'

                elif inp in ['6','6)','cerammic pot','ceramic']:
                    rx='ceramic'
                    rx1='ce'
                        
                elif inp in ['7','7)','metallic pot','metallic']:
                    rx='metallic'
                    rx1='m'
                elif inp in ['8','8)','concrete pot','conrete']:
                    rx='concrete'
                    rx1='co'
                elif inp in ['9','9)','seedling tray','seedling']:
                    rx='seedling'
                    rx1='se'
                elif inp in ['10','10)','grow bags','grow']:
                    rx='grow'
                    rx1='g'
                elif inp in ['11','11)','cutting tools','cutting','cutting tool']:
                    rx='cutting'
                    rx1='cu'
                elif inp in ['12','12)','hand tools','hand','hand tool']:
                    rx='hand'
                    rx1='ha'
                elif inp in ['13','13)','digging tools','digging tool','digging']:
                    rx='digging'
                    rx1='d'
                elif inp in ['14','14)','watering tools','watering tool','watering']:
                    rx='watering'
                    rx1='w'
                elif inp in ['15','15) fruits seeds','1','fruits','fruit','f']:
                    rx='fruit'
                    rx1='fr'      
                elif inp in ['16','16)','2) vegetable seeds','vegetables','vegetable','v']:
                    rx='vegetable'
                    rx1='v'
                
                else:
                    print('\t **$$** just press the given number or name **$$**\n ')
                    continue
                mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
                cursor=mycon.cursor()
                cursor.execute('select * from {}'.format(rx))
                data=cursor.fetchall()
                
                print()

                if n=='addt':

                    addt(n,rx,rx1)
                    continue

                for i in data:
                    print(i[0],')',i[1],'->',i[2])
                    mycon.close()
                
                if n=='home':
                    add(rx,rx1)
                    continue
                elif n=='homedrop':
                    dropt(rx,rx1)
                
                

        def today():
            print()
            print('\t ... . . YOU ARE IN TODAYS DEAL SECTION... . . \n')
            print()
            while True:
                print('\n\tTo go back press 0\n')
                print('1) ADD DEALS')
                print('2) DROP DEALS')
                print()
                deal_inp=input('.> ').lower().strip()
                if deal_inp in ['0','return','\q']:
                    return
                if deal_inp in ['add','add deal','1) add deals','1)','1','add deals']:
                    prin('addt')
                elif deal_inp in ['drop','drop deals','drop deals','2) drop deals','2)','2']:
                    dropt('todayd')

      
        def adid(id):
           
            for i in adminid:
                if i[0]==id:
                    return 'done'
            
            return 'not done'
        def pasd(pas):
            
            for i in adminid:
                if i[1]==pas:
                    return 'done'
            
            return 'not done'


        print('\t\t-you are in admin page-\n')
        
        while True:
            id=input('\t Enter your ID: ').lower().strip()
            ch=adid(id)
            if ch=='done':
                break
            else:
                print('\t !!! INCORECT ID !!!\n')
                continue
        while True:
            pas=input('\t Enter the Password: ').strip()
            ch=pasd(pas)
            if ch=='done':
                break
            else:
                print('\t !!! INCORECT PASSWORD !!!\n')
                continue
        print()
        print()

        print('*'*157)
        print('\t <<==|| ____GONA WORLD____ ||-.-|| ____GONA WORLD____ ||-.-|| ____GONA WORLD____ ||-.-|| ____GONA WORLD____ ||-.-|| ____GONA WORLD____ ||==>>')
        print('*'*157)
        print()
        print()
        print()

        mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
        cursor=mycon.cursor()
        cursor.execute('select count(*),sum(price) from cus_buy')
        data=cursor.fetchall()
        
        
        print('TOTAL SELL COUNT: ',data[0][0])
        print('TOTAL PRICE SOLD: ',data[0][1])
        mycon.close()
        print()
        print()

        # <<<<<<<<<<---------------- ADMIN PAGE ------------------>>>>>>>>>>>>

        while True:
            print('*'*157)
            print()
            print('\t\t\t\t\t\t\t\t<< -  TODAYS DEAL  - >>\n')
            print('\t\t\t\t\t\t\t\t<< -      ADD      - >>\n')
            print('\t\t\t\t\t\t\t\t<< -      DROP     - >>\n')
            print('\t\t\t\t\t\t\t\t<< - CUSTOMER LIST - >>\n')
            print('\t\t\t\t\t\t\t\t<< - PRODUCTS SOLD  - >>\n')
            print('\t\t\t\t\t\t\t\t<< -      EXIT     - >>\n')
            
            
            print()
            print('*'*157)

            adminp=input('=> ').lower().strip()
            if adminp in ['todays deal','deal','today','0','t','today deal']:
                today()
            elif adminp in ['add','1','a']:
                prin('home')
            elif adminp in ['drop','2','d']:
                prin('homedrop')
            elif adminp in ['3','c','customer list','customer']:
                cslist()
            elif adminp in ['4','p','product sold','products sold']:
                allsold()
            elif adminp in ['5','\q','exit']:
                mycon.close()
                return




    def user():
        
        
        def chckn(rx):
            mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
            if mycon.is_connected():
                pass
                    
            else:
                print('\n \t ### error in connecting try agian later ### \n')
            cursor=mycon.cursor()
            cursor.execute('select * from cus_info')
            data=cursor.fetchall()
            for i in data:
                if i[1]==rx:
                    return 'exist'

            mycon.close()
            return 'all clear'
            


        def chck(rx,tx):

            mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
            if mycon.is_connected():
                pass
                    
            else:
                print('\n \t ### error in connecting try agian later ### \n')

            cursor=mycon.cursor()

            cursor.execute('select * from cus_info')
            data=cursor.fetchall()
            for i in data:
                if i[1]==rx and dec.dec(i[2])==tx:
                    mycon.close()
                    return 'all is well'
                elif i[1]==rx and dec.dec(i[2])!=tx:
                    mycon.close()
                    return 'passwrd'
                elif i[1]!=rx:
                    pass
            mycon.close()
            return 'user_id'


        def passwup(rx,tx):
            
            tx1=enc.enc(tx)
            mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
            if mycon.is_connected():
                pass
            else:
                print('\n \t ### error in connecting try agian later ### \n')

            cursor=mycon.cursor()

            cursor.execute("update cus_info set cus_pass='{}' where cus_name='{}'".format(tx1,rx))
            mycon.commit()
            mycon.close()
                

        def passwc():
            #creating password'

            while True:
                print()

                user_pas=input("create a password :")
                if len(user_pas)<5:
                    print('\t !!! password is too small !!!\n')
                    continue
                if user_pas.isalpha() or user_pas.isdigit():
                    print('\t !!! use both numeric and alphabets !!!\n')
                    print('\t** you can also use special characters except(#!) **')
                    continue
                if '#!' in user_pas:
                    print("\t\t *** you can't use '#!' in your password *** \n")
                    continue
                        
                user_pas_ch=input("Confirm your password :")
        
                if user_pas_ch==user_pas:
                    print()
                    break
                else:
                    print()
                    print("\t !!! Password doesn't match !!! ")
                    print()
                    continue
            return user_pas



        def register():
            print('\t\t\t --- you are in registration portal --- \n')
            user_id=input('enter your name: ').title().lower().rstrip()
            na=chckn(user_id)
            if na=='exist':
                print()
                print('\t\t your name alredy exist\n')
                print('\t\t redirecting to the login portal\n')
                login()                                               ########## redirecting to login ------------------>>>>>>>>>>>>>>>>
                return
            elif na=='all clear':
                passwrd=passwc()
                passwrd1=enc.enc(passwrd)
                mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
                cursor=mycon.cursor()
                cursor.execute('select*from cus_info')
                cursor.fetchall()
                count=cursor.rowcount

                cs='cs{}'.format(count+1)

                cursor.execute("insert into cus_info values('{}','{}','{}')".format(cs,user_id,passwrd1))
                mycon.commit()
                mycon.close()

                global cs_id
                cs_id=csid.csid(user_id)

                print("\t\t !!! account created !!!\n")
                return

            else:
                print('** someting went wrong **')



        def login():


            print('--- your in login portal ---')
            c=0
            yc=1
            yd=1
            while True:
                print()
                user_id=input('user id:').lower().strip()
                passwrd=input('password:')

                nx=chck(user_id,passwrd)

                if nx=='all is well':
                    
                    global cs_id
                    cs_id=csid.csid(user_id)

                    print('\t** login sucessful **\n')
                    break

                elif nx=='passwrd':
                    print('\t\t # # # password incorrect # # #\n')
                    print('\t\t try again \n')
                    c+=1
                    if c>=3:
                        while True:

                            passr=input('\t Do you want to reset your password (yes/no):').lower().strip()
                            if passr in ['y','yes']:
                                p=passwc()
                                passwup(user_id,p)
                                print('\t\t *-*-* password updated sucessfully *-*-*\n')
                                yc=0
                                break
                            elif passr in ['no','n']:
                                break
                            else:
                                print('\t #`#just type (yes) or (no) #`# \n')
                                continue
                        if yc==0:
                            break
                    continue
            

                elif nx=='user_id':
                    print('<- your name not found ->\n')
                    print('- try registering your name -\n')
                    while  True:

                            ask=input('do you want to register(r) or not(n): ').lower().strip()
                            if ask=='r' or ask=='register':
                                print()
                                print('\t !! redirecting to registraion page !!\n')
                                register()
                                yd=0                                                    ####### redirect to register ------->>>>>
                                break

                            elif ask=='n' or ask=='no':
                                break
                            else:
                                print()
                                print("just say 'r' or 'n' ")
                                print()
                                continue
                    if yd==0:
                        break

            return
                
                                            ######## ------------->>>>>>>>>> 

        print()


        def homepage():

            def about_us():
                print()
                print("-="*64)
                print(" "*60 + "ABOUT US" + " "*60)
                print("-="*64)
                print()
                print("Thanks For using our Service, here is our About Us section:")
                print()
                print("We are GONA!, a service that aims to help you getting the best quality plants and products from the locals.")
                print('We have a wide variety of plants and its products, some exciting daily deals and all these at your finger tips.')
                print('\tHope you enjoy shopping\n')
                print("The Developer:")
                print("Sritish Kumar Gouda")
                print('Ritesh kumar Nayak')
                print("XII - A, Kendriya Vidyalaya, BAM")
                print("For Queries:")
                print("sritishkumargouda@gmail.com")
                print()
                while True:
                    
                    inp=input("Press 'r' to go back :").lower().strip()
                    if inp in ['r','back']:
                        return
                    else:
                        print("( just press 'r' or 'back' )\n")
                        continue
                    

            def profile(n):

                print()
                print(' ░░'*32+'\n')
                mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
                cursor=mycon.cursor()
                cursor.execute('select cus_name from cus_info where cus_id="{}"'.format(cs_id))
                data=cursor.fetchall()
                print('\t\t\t\t'+data[0][0]+'\n')
                cursor.execute('select * from cus_profile where cus_id="{}"'.format(cs_id))
                data=cursor.fetchall()

                if len(data)==0:
                    print()
                    print('\t\t *!*!* your profile is empty try fillig it *!*!* \n')
                    if n=='home':
                        chck=input('Press 0 to go back or press enter to fill your profile - ').lower().strip()

                        if chck in ['0','no']:
                            mycon.close()
                            return
                            
                    while True:
                            
                        phone=input('Enter you phone number: ').strip()
                        pincode=input('Enter your pincode :').strip()

                        if pincode.isdigit() and phone.isdigit():
                            pass
                        else:
                            print()
                            print('\t !!! cant use alphabets or characters in number !!!')
                            continue

                        if len(phone)!=10:
                            print()
                            print('\t !!!! Invalid Phone Number !!!\n')
                            continue

                        if len(pincode)!=6:
                            print()
                            print('\t !!!! Invalid Pincode !!!\n')
                            continue

                            
                        elif len(pincode)==6 and len(phone)==10:
                            break
                            
                    faddress=''		
                    while True:
                            
                        state=input('Enter your State :').upper().strip()
                        city=input('Enter your City :').lower().strip()
                        address=input('Enter your Address :').lower().strip()
                        landmark=input('Enter any Landmark(optional) : ').lower().strip()

                        if state.isalpha() or city.isalpha():
                            pass
                        else:
                            print()
                            print('\t !!! Invalid State name or City name !!!\n')
                            continue

                        if len(state)==0 or len(city)==0 or len(address)==0:
                            print()
                            print('\t !!! all fields are mandatory !!!\n')
                            continue
                        break
                    faddress+=address+','+city+','+state+','+landmark
                    while  True:
                        email=input('Enter your email : ').lower().strip()

                        if '@' not in email or '.' not in email or email in ['.@','@.']:
                            print('\t !!!! Invalid email id !!!\n')
                            continue


                        elif len(email)==0:
                            print('\t !!! cant be left blank\n')
                            continue
                        break

                    cursor.execute("insert into cus_profile values('{}','{}',{},'{}',{})".format(cs_id,faddress,pincode,email,phone))
                    mycon.commit()
                    print()
                    print()
                    print('\t\t *** SUCESSFULLY UPDATED YOUR PROFILE ***\n')
                    mycon.close()
                    print()
                    for i in data:
                        print('Address: ',i[1])
                        print('Pincode: ',i[2])
                        print('Phone number: ',i[4])
                        print('Email id: ',i[3])
                        print()
                    time.sleep(2)
                    

                    return

                else:

                    print()
                    for i in data:
                        print('Address: ',i[1])
                        print('Pincode: ',i[2])
                        print('Phone number: ',i[4])
                        print('Email id: ',i[3])
                        print()
                    if n=='home':

                        print('\t\t -||- YOUR ORDERS -||-\n')
                        cursor.execute('select name,price from cus_buy where cus_id="{}"'.format(cs_id))
                        dt=cursor.fetchall()
                        for i in dt:
                            print(i[0],'->',i[1])
                    time.sleep(3)
                print()
                again=input('DO YOU WANT TO CHANGE YOUR pROFILE: ').lower().strip()
                if again in ['yes','y']:
                    cursor.execute('delete from cus_profile where cus_id="{}"'.format(cs_id))  
                    mycon.commit()
                    profile('home')
                    mycon.close()
                    return

                mycon.close()
                return


            def bill():

                def buy():
                    mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
                    cursor=mycon.cursor()
                    cursor.execute('select * from cus_cart where cus_id="{}"'.format(cs_id))
                    dt=cursor.fetchall()
                    cursor.execute('delete from cus_cart where cus_id="{}"'.format(cs_id))
                    mycon.commit()
                    buyi=[]
                    for i in dt:
                        cursor.execute('insert into cus_buy values("{}","{}","{}",{})'.format(cs_id,i[1],i[2],i[3]))
                        buyi.append((i[2],i[3]))
                        mycon.commit()
                    return buyi


                print('='*155)
                print('\t\t\t\t\t\t\t\t BILLING PAGE ')
                print('='*155)
                mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
                cursor=mycon.cursor()
                cursor.execute('select sum(price) as total from cus_cart where cus_id="{}"'.format(cs_id))
                data=cursor.fetchall()
                total=data[0][0]
                print('\t\t YOUR TOTAL: ',total)
                while True:
                    print('\tpress "0" to return\n')
                    chck=input('\t press enter to confirm ').lower().rstrip()

                    if chck in ['',' ','yes','y','confirm']:
                        break
                    elif chck in ['no','n','0','return']:
                        return '1st'
                    else:
                        print('\t !!! just press enter or type "yes" !!!\n')
                        continue
                profile('bill')
                print()
                print('\t\t $ #### $  DILEVERY CHARGES $ #### $\n')
        
                print('1) standard dilevery charges - 75')
                print('In standard dilevery you will get your order within 2-3 week\n')
                print('2) prime dilevery charges    - 100')
                print('In prime dilevery you will get your within 5 days\n')

                
                while True:
                    print('\tpress "0" to return to your cart')
                    dil=input('\tENETR THE TYPE OF DILEVERY YOU WANT :').lower().strip()
                    if dil=='1' or dil=='standard dilevery charges' or dil=='standard dilevery' or  dil=='standard':
                        total+=75
                        break
                        
                        
                    elif dil=='2' or dil in 'prime dilevery charges' or dil=='prime dilevery' or dil=='prime':
                        total+=100
                        break
                    elif dil in ['0','return']:
                        return '1st'

                    else:
                        print('\t just press 1 or 2\n')
                        continue
                print('.'*70)
                print('\n\n\n')
                print('\t\t YOUR TOTAL: ',total)
                print('\tSelect the mode of payment\n')
                print('1) credit/debit card ')
                print('2) UPI payment')
                print('3) cash on dilevery (COD)\n')

                pay=input('Enter your mode of payment :').lower().strip()
                if pay in ['1','cerdit card','credit','debit card','debit']:
                    while True:

                        print()
                        print('\t  -- card payment -- \n')

                        card_no=input('ENTER CARD NUMBER : ')
                        card_ex=input('ENTER THE EXPIRY DATE: ')
                        card_name=input('ENTER THE NAME OF CARD HOLDER NAME :')
                        card_cvv=input('ENTER THE CVV NO.')
                        if card_no.isdigit() and card_cvv.isdigit():
                            break 
                        if len(card_no)==0 or len(card_cvv)==0 or len(card_ex)==0 or len(card_name)==0:
                            print("\t !! This can't be left blank\n")
                            continue
                        else:
                            print('\t!!! Accepts only int !!!\n')
                            continue
                elif pay=='2' or pay in ['upi payment','upi']:

                    print('\t upi payment \n')
                    print('\t\n total price :',total)
                    print('\t UPI id - gona123@oksbi')
                    time.sleep(3)

                elif pay=='3' or pay in 'cash on dilevery COD':
                    print('\t\n total price :',total)
                    print('\t\t Cash on dilevery \n\n')
                    time.sleep(3)
                
                while True:
                    print('\tpress "0" to return to your cart')
                    pay_c=input('CONFIRM ORDER(yes/no): ').lower().strip()
                    if pay_c=='yes' or pay_c=='y':
                        break
                    elif pay_c=='no' or pay_c=='n':

                        continue
                    elif pay_c=='0' or pay_c=='return':
                        return '1st'
                    else:
                        print('\t!! YES OR NO ONLY !!\n')
                        continue

                while True:
                    print()
                    caps=''
                    for i in range(0,2):
                        a=random.randint(65,90)
                        caps+=chr(a)
                        b=random.randint(97,122)
                        caps+=chr(b)
                        c=random.randint(0,9)
                        caps+=str(c)
                   
                    print('\t\t',caps)
                    print('\tpress "r" to relode captha')
                    cap_c=input('Enter the captcha carefully : ').strip()
                    if cap_c in ['r','R','relode']:
                        continue
                    if cap_c==caps:
                        break
                    else:
                        print()
                        print('--TRY AGAIN --')
                        continue
                print()
                print(' - transcation in process just wait - \n')
                print('\t\t.... L',end='')
                time.sleep(1)
                print(' O A D ',end='')
                time.sleep(1)
                print('I N G',end='')
                time.sleep(2)
                print(' ....')
                print()

                print('\t\t!!!  SUCESSFUL !!!\n')
                time.sleep(0.5)

                with open('bill.txt','w') as f:

                    f.write('='*70+'\n')
                    f.write('\t\t\t\tBILL\n')
                    f.write('='*70+'\n\n')
                    cursor.execute('select cus_info.cus_name,phone,address,pincode,emailid from cus_info,cus_profile where cus_info.cus_id=cus_profile.cus_id and cus_profile.cus_id="{}"'.format(cs_id))
                    data=cursor.fetchall()
                    buyi=buy()
                    for i in data:
                        print('Name: ',i[0])
                        f.write('Name: '+str(i[0])+'\n')
                        print('Address: ',i[2])
                        f.write('Address: '+str(i[2])+'\n')
                        print('Pincode: ',i[3])
                        f.write('Pincode: '+str(i[3])+'\n')
                        print('Phone: ',i[1])
                        f.write('Phone: '+str(i[1])+'\n')
                        print('Email id: ',i[4])
                        f.write('Email id: '+str(i[4])+'\n')
                    print('\t\t -||- your order -||-\n')
                    f.write('\t\t -||- your order -||-\n')
                    for i in buyi:
                        print(i[0],'->',i[1])
                        f.write(i[0]+'->'+str(i[1])+'\n')
                    
                        

                    print()
                    cursor.execute('select * from cus_cart where cus_id="{}"'.format(cs_id))
                    data=cursor.fetchall()
                    for i in data:
                        print(i[2],'->',i[3])
                    print()
                    print('Total price: ',total)
                    
                    f.write('='*70+'\n')
                    f.close()

                os.system('bill.txt')
                
                return '2nd'
                


            def carta(n):
                while True:

                    mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
                    cursor=mycon.cursor()
                    
                    def cartp(n):
                        mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
                        cursor=mycon.cursor()
                        cursor.execute("select product_id,name,price from cus_cart where cus_id='{}'".format(n))
                        data=cursor.fetchall()
                        c=1
                        print(' ░░|'*16+'\n')
                        print(' ░░| \t\t\t  - |YOUR CART | - \t\t\t\n')
                        for i in data:
                            
                            c=0
                            print(' ░░|',i[0],')',i[1],'=>',i[2],'\n')
                        if c==1:       
                            print(' ░░| \t\t *!* YOUR CART IS EMPTY *!* \t\t\n')
                        print(' ░░|'*16+'\n')
                        mycon.close()
                        return

                    cartp(n)

                    time.sleep(5)

                    chz=1 
                    while True:
                        print('\t - - press 0 to go back - -\n')
                        chck=input('\t DO YOU WANT TO PROCEED(p) OR REMOVE(r) SOME ITEMS :').lower().strip()
                        if chck in ['0']:
                            mycon.close
                            return
                        elif chck in ['yes','p','proceed']:
                            mycon.close
                            chx=bill()
                            if chx=='1st':
                                chz=2
                                break
                            if chx=='2nd':
                                chz=3
                                break
                            continue

                        elif chck in ['no','r','remove']:
                            print()
                            print()
                            print('\t - - press 0 to go back - -')
                            while True:
                                print()
                                print("if you want to remove multiple items then give ',' in between them\n")
                                inp1=input('Enter the Sl No. of the item(s) you want to remove ->').lower().strip()
                                inp=inp1.split(',')
                                cursor.execute('select count(*) from cus_cart')
                                data=cursor.fetchall()
                                rx=data[0][0]
                                #print(rx)
                                c=0
                                
                                for i in inp:
                                    cursor.execute("delete from cus_cart where product_id='{}'".format(i))
                                    mycon.commit()
                                    cursor.execute('select count(*) from cus_cart')
                                    data1=cursor.fetchall()
                                    tx=data1[0][0]
                                    #print(tx)
                                    if rx==tx:
                                        c+=1
                                cartp(n)
                                if '0' in inp:
                                    break
                                if c>0:
                                    print()
                                    print(c,'- items not found - ')
                                    print('\t *** try again ***')
                                    print()
                                    continue
                                break
                            
                            continue


                                
                        else:
                            print("#-#- just press 'p' or 'r' -#-#")

                            continue
                    if chz==2:
                        continue
                    elif chz==3:
                        break 
                return   
           


            def all(rx,rx1):
                mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
                cursor=mycon.cursor()
                    

                cursor.execute('select * from {}'.format(rx))
                data=cursor.fetchall()
                count=cursor.rowcount
                tx=[]
                x=len(rx1)
                print()
                for i in data:
                    tx+=[i]
                    print(i[0][x::],')',i[1],'-->>',i[2])

                y='y'
                while True:
                    print('\t - press "0" to go back -\n')
                    print("\t if you want to buy multiple items then you can write them in between commas','\n")
                    inp=input('=>').lower().rstrip().split(',')
                    if inp=='0':
                            return
                    for i in inp:
                        
                        if i.isdigit():
                            

                            cursor.execute("select * from {} where product_id='{}'".format(rx,rx1+i))
                            data=cursor.fetchall()

                            if len(data)==0:
                                print()
                                print('\t *** # just type the name or number from the given list # *** \n')
                                y='again'
                                break

                            print(data[0][1])
                            cursor.execute("insert into cus_cart values('{}','{}','{}',{})".format(cs_id,data[0][0],data[0][1],data[0][2]))
                            mycon.commit()
                            y='y'
                            
                            
                        
                        elif i in ['pots','bag','seedling','seeds','seed','tray','seedling tray','ceramic pot','grow bag','planter','plants','plant','holes','steel','cultivator','rake','pipe']:
                            print()
                            print('\t *** # just type the name or number from the given list # *** \n')
                            print("\t\t ### you cant type 'plant(s)' ###\n")
                            y='again'
                            break

                        elif i.isalpha():
                            
                            cursor.execute("select * from {} where name like '%{}%'".format(rx,i))
                            data=cursor.fetchall()
                            if len(data)==0:
                                print()
                                print('\t *** # just type the name or number from the given list # *** \n')
                                y='again'
                                break

                            print(data[0][1])
                            cursor.execute("insert into cus_cart values('{}','{}','{}',{})".format(cs_id,data[0][0],data[0][1],data[0][2]))
                            mycon.commit()
                            y='y'
                            

                        
                        elif i.isalnum():
                            
                            cursor.execute("select * from {} where name or product_id like '%{}%'".format(rx,i))
                            data=cursor.fetchall()
                            if len(data)==0:
                                print()
                                print('\t *** # just type the name or number from the given list # *** \n')
                                y='again'
                                break

                            print(data[0][1])
                            cursor.execute("insert into cus_cart values('{}','{}','{}',{})".format(cs_id,data[0][0],data[0][1],data[0][2]))
                            mycon.commit()
                            y='y'
                            
                       

                        else:

                            print()
                            print('\t *** # just type the name or number from the given list # *** \n')
                            y='again'
                            break


                    if y=='again':
                        continue

                    mycon.close()
                    break
                return

            
            def seeds(v=None):
                print('\t\t -.-.- you are in the seeds section -.-.- \n')
                print()
                while True:

                    print('\n\tTo go back press 0\n')
                    print('1) FRUITS SEEDS')
                    print('2) VEGETABLE SEEDS')

                    seedinp=input('enter: ').lower().strip()
                
                    if seedinp in ['0','back']:
                        return

                    elif seedinp in ['1)','1) fruits seeds','1','fruits','fruit','f']:
                        rx='fruit'
                        rx1='fr'      
                    elif seedinp in ['2','2)','2) vegetable seeds','vegetables','vegetable','v']:
                        rx='vegetable'
                        rx1='v'      
                    else:
                        print('\t **$$** just press the given number or name **$$**\n ')
                        continue
                    all(rx,rx1)


            def tools():
                print('\t\t -.-.- you are in the tools section -.-.- \n')
                print()
                while True:

                    print('\n\tTo go back press 0\n')
                    print('1) CUTTING TOOLS')
                    print('2) HAND TOOLS')
                    print('3) DIGGING TOOLS')
                    print('4) WATERING TOOLS')
                   

                    toolinp=input('enter: ').lower().strip()

                    if toolinp in ['0','back']:
                        return
                    elif toolinp in ['1','1)','cutting tools','cutting','cutting tool']:
                        rx='cutting'
                        rx1='cu'
                    elif toolinp in ['2','2)','hand tools','hand','hand tool']:
                        rx='hand'
                        rx1='ha'
                    elif toolinp in ['3','3)','digging tools','digging tool','digging']:
                        rx='digging'
                        rx1='d'
                    elif toolinp in ['4','4)','watering tools','watering tool','watering']:
                        rx='watering'
                        rx1='w'
                    else:
                        print('\t **$$** just press the given number or name **$$**\n ')
                        continue
                    all(rx,rx1)


            def pots():

                print('\t\t -.-.- you are in the pots section -.-.- \n')
                print()

                while True:

                    print('\n\tTo go back press 0\n')
                    print('1) Ceramic Pots')
                    print('2) Metallic Pots')
                    print('3) Concrete Pots')
                    print('4) Seedling Tray')
                    print('5) Grow Bags')
                    potinp=input('enter: ').lower().strip()

                    if potinp in ['0','back']:
                        return
                    elif potinp in ['1','1)','cerammic pot','ceramic']:
                        rx='ceramic'
                        rx1='ce'
                        
                    elif potinp in ['2','2)','metallic pot','metallic']:
                        rx='metallic'
                        rx1='m'
                    elif potinp in ['3','3)','concrete pot','conrete']:
                        rx='concrete'
                        rx1='co'
                    elif potinp in ['4','4)','seedling tray','seedling']:
                        rx='seedling'
                        rx1='se'
                    elif potinp in ['5','5)','grow bags','grow']:
                        rx='grow'
                        rx1='g'
                    else:
                        print('\t **$$** just press the given number or name **$$**\n ')
                        continue
                    all(rx,rx1)
                    
            

            def plants():
                

                print('\t\t -.-.- you are in the plants section -.-.- \n')
                print()
                

                while True:

                    print('\n\tTo go back press 0\n')
                    print("1) LOW MAINTENANCE PLANTS")
                    print("2) FOLIAGE PLANTS")
                    print("3) INDOOR PLANTS")
                    print("4) AIR PURIFIER PLANTS")
                    print("5) FLOWERING \n\n")

                    plantinp=input('enter: ').lower().strip()

                    if plantinp=='0':
                        return
                    elif plantinp in ['1)','1','low maintenance plants','low','low maintenance','low maintenance plant']:
                        rx='lowp'
                        rx1='l'
                    elif plantinp in ['2)','2','foligae plants','foliage plant','foliage']:
                        rx='folp'
                        rx1='f'
                    elif plantinp in ['3)','3','indoor plants','indoor','indoor plant',]:
                        rx='indp'
                        rx1='i'
                    elif plantinp in ['4)','4','air purifier plants','purifier','purifier plant',]:
                        rx='airp'
                        rx1='a'
                    elif plantinp in ['5)','5','flowering plants','flowering','flowering plant',]:
                        rx='flop'
                        rx1='fl'
                    else:
                        print('\t **$$** just press the given number or name **$$**\n ')
                        continue
                    all(rx,rx1)

            def todaydeals():
                print('\t\t -.-. YOUR IN TODAYS DEALS SECTION .-.-\n')
                mycon=mysql.connect(host='localhost',user='root',passwd='root',database='gona')
                cursor=mycon.cursor()
                cursor.execute('select * from todayd')
                data=cursor.fetchall()
                for i in data:
                    print(i[0],')',i[1],'-> Rs.',i[3],'[',i[2],']')
                while True:
                    print('\t - press "0" to go back -\n')
                    print("\t if you want to buy multiple items then you can write them in between commas','\n")
                    inp=input('=>').lower().rstrip().split(',')
                    pos=''
                    if '0' in inp or 'back' in inp:
                        mycon.close()
                        return
                    for i in inp:

                        if i in ['pots','bag','seedling','seeds','seed','tray','seedling tray','ceramic pot','grow bag','planter','plants','plant','holes','steel','cultivator','rake','pipe']:
                            print('\t !!! INVALID NAME {} !!!\n'.format(i))
                            pos+='neg'
                            continue
                        if i.isdigit():
                            print('\t !!! INVALID ID {} !!!\n'.format(i))
                            pos+='neg'
                            continue
                        elif i.isalpha():
                            
                            cursor.execute('select * from todayd where name like "%{}%"'.format(i))
                            data=cursor.fetchall()
                            if len(data)==0:
                                print('\t !!! INVALID NAME {} !!!\n'.format(i))
                                pos+='neg'
                                continue
                            print(data)
                            cursor.execute('insert into cus_cart values("{}","{}","{}",{})'.format(cs_id,data[0][0],data[0][1],data[0][3]))
                            mycon.commit()    
                            pos+='pos'
                            
                            
                        elif i.isalnum():
                            
                            cursor.execute('select * from todayd where product_id="{}" or name like "%{}%"'.format(i,i))
                            data=cursor.fetchall()
                            if len(data)==0:
                                print('\t !!! INVALID ID/NAME {} !!!\n'.format(i))
                                pos+='neg'
                                continue
                            print(data)
                            cursor.execute('insert into cus_cart values("{}","{}","{}",{})'.format(cs_id,data[0][0],data[0][1],data[0][3])) 
                            mycon.commit()   
                            pos+='pos'
                            
                            
                        else:
                            print('\t !!! INVALID KEY {} !!!\n'.format(i))
                            pos+='neg'
                            continue
                    if 'pos' in pos:
                        print('\t ### added to your cart ###\n')
                        break
                    else:
                        continue

                

            ############## <-----------> HOME PAGE <-------------> ################# 

            
            print()

            while True:
                print('__'*77)
                print()
                print('''
        \t\t\t\t\t#*#*#*#*#*#    #*#*#*#*#*#    #*       *#    #*#*#*#*#*#
        \t\t\t\t\t#*             #*       *#    #* *     *#    #*       *#
        \t\t\t\t\t#*             #*       *#    #*  *    *#    #*       *#
        \t\t\t\t\t#*   *#*#*#    #*       *#    #*   *   *#    #*#*#*#*#*#
        \t\t\t\t\t#*       *#    #*       *#    #*    *  *#    #*       *#
        \t\t\t\t\t#*       *#    #*       *#    #*     * *#    #*       *#
        \t\t\t\t\t#*#*#*#*#*#    #*#*#*#*#*#    #*       *#    #*       *#''')
                print()
                print('__'*77)
                print()
                print('\t\t\t\t\t\t\t\t<< -  TODAYS DEAL - >>\n')
                print('\t\t\t\t\t\t\t\t<< -    PLANTS    - >>\n')
                print('\t\t\t\t\t\t\t\t<< -     POTS     - >>\n')
                print('\t\t\t\t\t\t\t\t<< -    TOOLS     - >>\n')
                print('\t\t\t\t\t\t\t\t<< -    SEEDS     - >>\n')
                print('\t\t\t\t\t\t\t\t<< -  YOUR CART   - >>\n')
                print('\t\t\t\t\t\t\t\t<< -   PROFILE    - >>\n')
                print('\t\t\t\t\t\t\t\t<< -   ABOUT US   - >>\n')
                print('\t\t\t\t\t\t\t\t<< -     EXIT     - >>\n') 

                hominp=input('=>').lower().rstrip()

                if hominp in ['todays deal','deal','deals','t','0']:
                    todaydeals()

                if hominp in ['plants','plant','1']:
                    plants()
                elif hominp in ['pots','pot','2']:
                    pots()
                elif hominp in ['tools','tool','3']:
                    tools()
                elif hominp in ['seeds','seed','4']:
                    seeds()
                elif hominp in ['your cart','c','cart']:
                    carta(cs_id)
                elif hominp in ['about us','a','about']:
                    about_us()

                elif hominp in ['profile','p']:
                    profile('home')

                elif hominp in ['exit','e',]:
                    return


        while True: 
            print()                                                           # main ######################
            userchck=input('\t\tLOGIN OR REGISTER : ').lower().rstrip()
            if userchck in ['register','r','reg']:
                register()
                homepage()
                return
            elif userchck in ['login','log','l']:
                login()
                homepage()
                return
            elif userchck in ['0','return']:
                return
            else:
                print('\t\t -- just type login or register --\n')
                continue



    print('########################################################################  WELCOME  TO  OUR  WORLD  #######################################################################')
    print()
    while True:
        usad=input('\t\t\tUSER OR ADMIN : ').lower().rstrip()
        print()
        if usad in ['user','u']:
            user()
            print('all went  right')
            continue
            
        elif usad in ['admin','a']:
            admin()
            print('all went  right')
            continue

        elif usad in ['\q']:
            return

        else:
            print('\t\t -- just type user or admin please --\n')
            continue
        

main()
