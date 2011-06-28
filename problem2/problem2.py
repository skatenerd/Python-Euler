import fibo

def isEven(x):
    return x%2==0

fiboList =  fibo.fib(4000000)

evenFibs = filter(isEven, fiboList)

evenFibsSum = sum(evenFibs)

print(evenFibsSum)
