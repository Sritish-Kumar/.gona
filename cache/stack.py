
stack=[]
top=None
while True:
    print('\t\t .... STACK ....\n')

    def push():
        if len(stack)>=5:
            print('\t STACK OVERFLOW \n')
            return
        ele=eval(input('enter the element to be added: '))
        stack.append(ele)
        print(stack)
        global top
        top=len(stack)-1

    def pop():

        if len(stack)==0:
            print('\t STACK UNDERFLOW\n')
            return

        stack.pop()
        global top
        top-=1
    def peek():
        if len(stack)==0:
            print('\t STACK UNDERFLOW\n')
            return
        rx=stack[top]
        return rx
    
    def display():
        if len(stack)==0:
            print('\t STACK UNDERFLOW \n')
            return
        print('\t STACK -> ')
        print(stack[::-1])


    print('\t 1. PUSH ')
    print('\t 2. POP')
    print('\t 3. peek')
    print('\t 4. Display')
    print('\t 5. exit')

    ch=input('=>').lower().strip()

    if ch in ['1.','1','push']:
        push()
    elif ch in ['2.','2','pop']:
        pop()
    elif ch in ['3.','3','peek']:
        tx=peek()
        print(f'element:{tx}')
    elif ch in ['4.','4','display']:
        display()
    elif ch in ['5.','5','exit']:
        break
    else:
        print('## INVALID INPUT')
        continue


stack={}
top=0
while True:
    print('... STACK ...')

    def push():
        if len(stack)>=5:
            print('\t stack overflow\n')
            return
        ele=input('enter: ')
        global top
        stack[top]=ele
        
        top=len(stack)
        print(stack)
        print(top)

    def pop():
        if len(stack)==0:
            print('\t stack underflow\n')
            return
        stack.popitem()
        global top 
        top-=1

    def peek():
        if len(stack)==0:
            print('\t stack underflow\n')
            return
        
        rx=stack[top-1]
        return rx
    def display():
        if len(stack)==0:
            print('\t stack underflow\n')
            return
        for i in range(top-1,-1,-1):
            print(stack[i])


    print('press 1.push\n 2.pop\n 3.peek\n 4.display\n ')
    ch=input('->').lower()

    if ch=='1':
        push()
    elif ch=='2':
        pop()
    elif ch=='3':
        tx=peek()
        print(tx)
    elif ch=='4':
        display()        



