array = input()
buffer = ""
num = 0
numArray = []
q = []


def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def pow(a, b):
    return a ** b


for c in array:
    if(c != '+' and c != '-' and c != '*' and c != '/'):
        buffer += c
        if( c == array[-1]):
            numArray.append(float(buffer))
        continue
    numArray.append(float(buffer))
    buffer = ""
    q.append(c)


for i in range(0,len(q)):       #sdelat vyvod normalno
    a = numArray[i]
    b = numArray[i+1]
    c = q[i]
    if(c == "+"):
        sum(a,b)
    if(c == "-"):
        sub(a,b)
    if(c == "*"):
        mul(a,b)
    if(c == "/"):
        div(a,b)
    if(c == "^"):
        pow(a,b)

    





