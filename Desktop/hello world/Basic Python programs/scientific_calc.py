import math
def sum(a, b):
    return a + b

def substract(a, b):
    return a -b
def divide(a, b):
    return a/b

def multiplication(a, b):
    return a * b

def squr(a):
    return a**2

def sin(a):
    result = math.sin(a)
    return result

def cos(a):
    result = math.cos(a)
    return result
def tan(a):
    result = math.tan(a)
    return result
print(""" 
1 - sum(a,b)
2 - substract(a,b)
3 - divide(a,b)
4- Square(a)
5 - sin(a)
6 - cos(a)
7 - tan(a)
""")
op = int(input('Enter the number of operation to perform: '))

while op < 10:
    if op == 1:
        print('enter the values of a,b')
        a1 = int(input('Enter the value of a1: '))
        b1 = int(input('Enter the value of b1: '))
        res1 = sum(a1,b1)
        print(res1)
    elif op == 2:
        print('enter the values of a,b')
        a2 = int(input('Enter the value of a: '))
        b2 = int(input('Enter the value of b: '))
        res2 = substract(a2, b2)
        print(res2)
    elif op == 3:
        print('enter the values of a,b')
        a3 = int(input('Enter the value of a: '))
        b3 = int(input('Enter the value of b: '))
        res3 = divide(a3, b3)
        print(res3)
    elif op == 4:
        print('enter the values of a,b')
        a4 = int(input('Enter the value of a: '))
        res4 = squr(a4)
        print(res4)
    elif op == 5:
        print('enter the values of a,b')
        a5 = int(input('Enter the value of a: '))
        res5 = sin(a5)
        print(res5)
    elif op == 6:
        print('enter the values of a,b')
        a6 = int(input('Enter the value of a: '))
        res6 = cos(a6)
        print(res6)
    elif op == 7:
        print('enter the values of a,b')
        a7 = int(input('Enter the value of a: '))
        res7 = tan(a7)
        print(res7)
    else:
        print('choose an operation')

    new = int(input('do you want to continue - (yes - 1),(no - 0)'))
    if new == 1:
        op= int(input("enter the operation :"))
    elif new == 0:
        print('Thank you for using the scientific calculater')
    else:
        print('enter the right values either 1 or 0')
        new = int(input('do you want to continue - (yes - 1),(no - 0)'))

