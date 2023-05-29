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
       
