def sum1(first, second):
    return first + second

def sub(first, second):
    return first - second

def mul(first, second):
    return first * second

def div(first, second):
    return first / second

def pwr(first, second):
    return first ** second

def parse_array(array):
    buffer = ""
    num_array = []
    q = []
    for char in array:
        if char != '+' and char != '-' and char != '*' and char != '/' and char != '^':
            buffer += char
            if char == array[-1]:
                num_array.append(float(buffer))
            continue
        num_array.append(float(buffer))
        buffer = ""
        q.append(char)
    return num_array, q

def operate(_numbers, _operations, _input_array):
    a = _numbers[0]

    if len(_operations) == len(_numbers) and _operations[0] == _input_array[0] and _operations[0] == "-":
        a *= -1
        _operations.pop(0)

    for i in range(0,len(_operations)):
        b = _numbers[i+1]
        operation = _operations[i]
        if operation == "+":
            a = sum1(a, b)
            continue
        if operation == "-":
            a = sub(a,b)
            continue
        if operation == "*":
            a = mul(a,b)
            continue
        if operation == "/":
            a = div(a,b)
            continue
        if operation == "^":
            a = pwr(a, b)
            continue

    return a

input_array = input()
numbers, operations = parse_array(input_array)
answer = operate(numbers, operations, input_array)
print(answer)