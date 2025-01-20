# Sveiki atvykę į Skaičiuotuvą!

def add(first, second):
    return first + second

def sub(first, second):
    return first - second

def mul(first, second):
    return first * second

def div(first, second):
    return first / second

def pwr(first, second):
    return first ** second
try:
    assert add(2, 3) == 5, f"Klaida vykdant funkciją 'sum()'. Atsakymas turi būti {5}"
    assert sub(17, 10) == 7, f"Klaida vykdant funkciją 'sub()'. Atsakymas turi būti {7}"
    assert mul(5, 5) == 25, f"Klaida vykdant funkciją 'mul()'. Atsakymas turi būti {25}"
    assert div(81, 9) == 9, f"Klaida vykdant funkciją 'div()'. Atsakymas turi būti {9}"
    assert pwr(12, 2) == 144, f"Klaida vykdant funkciją 'pow()'. Atsakymas turi būti {144}"
    print(f'Visi testai yra sėkmingi')
except AssertionError as klaida:
    print(f"Testas: {klaida}")

def parse_array(array):
    buffer = ""
    num_array = []
    q = []
    for char in array:
        if char.isdigit():
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
            a = add(a, b)
            continue
        elif operation == "-":
            a = sub(a,b)
            continue
        elif operation == "*":
            a = mul(a,b)
            continue
        elif operation == "/":
            a = div(a,b)
            continue
        elif operation == "^":
            a = pwr(a, b)
            continue

    return a

def initiate(input_array): #easier for debugging and checks
    numbers, operations = parse_array(input_array)
    answer = operate(numbers, operations, input_array)
    print(answer)

initiate(input())
