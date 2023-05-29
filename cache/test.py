#STACK 
# lifo
# both data is added and removed from the last
# is  a way of orginizing data

'''print('STACK')

stack=[]
top= None

def push():
    if len(stack)>=10:
        print('stack overflow')
        return
    ele=input('enter the element: ')
    global top
    stack.append(ele)
    top=len(stack)-1

def pop():
    if len(stack)==0:
        print('stack underflow')
        return
    global top
    stack.pop()
    top-=1
def peek():
    if len(stack)==0:
        print('stack underflow')
        return
    peeked=stack[top]
    return peeked
def display():
    if len(stack)==0:
        print('stack underflow')
        return
    print(stack[::-1])

main=input('=>')
if main=='push':
    push()
elif main=='pop':
    pop()
elif main=='peek':
    peek()
elif main=='display':
    display()'''


print('stack')
stack=[]
top=None
size=5

def push():
    if len(stack)>size:
        print('\t STACK OVERFLOW\n')
        return
    ele=input('enter the element: ')
    stack.append(ele)
    global top
    top=len(stack)-1

    print(f'element {ele} added to stack')

def pop():
    if len(stack)==0:
        print('\t stack underflow\n')
        return
    print('popped element:',stack.pop())
    global top
    top=len(stack)-1

def display():
    if len(stack)==0:
        print('\t stack underflow\n')
        return

    print(stack[::-1])

def peek():
    if len(stack)==0:
        print('\t stack underflow\n')
        return
    print('peeked element: ',stack[top])
while True:
    chck=(input('enter: '))
    if chck in ['pop']:
        pop()
    elif chck in ['push']:
        push()

    elif chck in ['display']:
        display()
    elif chck in ['peek']:
        peek()


