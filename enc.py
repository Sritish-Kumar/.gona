def enc(rx):
    
    rx1='`1cd'
    for i in range(0,len(rx)):
        c=rx[i]
        rx1+=chr(ord(c)+1)+chr(ord(c)-1)+'#!'

    return rx1+'0cd`'
    

