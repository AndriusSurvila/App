

array = input()
buffer = ""
num = 0
numArray = []
q = []

for c in array:
    if(c != '+' and c != '-' and c != '*' and c != '/' or c == array[1:]):
        buffer += c
        continue
    numArray.append(float(buffer))
    buffer = ""
    q.append(c)

for i in range(0,len(q)):
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

    






def sum(a, b0):
