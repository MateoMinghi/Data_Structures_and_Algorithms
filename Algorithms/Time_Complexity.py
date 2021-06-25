import time
import sys

#these functions return the fibonacci numbers of a number 

def fib(n):    # write Fibonacci series up to n
    a = 0 
    b = 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    else:
        resultado = fibonacci(n - 1) + fibonacci(n - 2,)
        return resultado


#over here we assign n with a large value (25)
#that takes a lot of operations, therefore we must choose the correct method to implement it

if __name__ == '__main__':
    n = 25
    sys.setrecursionlimit(n + 10)

    startingTime = time.time()
    fib(n)
    endTime = time.time()
    print(f"Execution time with loop\t{endTime - startingTime}");

    startingTime = time.time()
    fibonacci(n)
    endTime = time.time()
    print(f"Execution time with recursion\t{endTime - startingTime}");
