def hello(x):
    if x == 0:
        return
    else:
        print("Hello")
        hello(x-1)

hello(4)

def sum(x):
    if x == 0:
        return 0
    elif x == 1:
        return 2
    else:
        return x + sum(x-1)

z = sum(4)
print(z)

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(3))

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

print(fibo(49))