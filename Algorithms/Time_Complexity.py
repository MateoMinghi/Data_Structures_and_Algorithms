import time
import sys

#these functions return the factorial of a number 
#factorial is a function that multiplies a number by every number below it

def factorial_1(n):
  if n == 0:
    return 1
  else:
    return n * factorial_1(n - 1)

def factorial(n):
    response = 1
    while n > 1:
        response = response * n
        n = n - 1
    return response


#over here we assign n with a large value (2500)
#that takes a lot of operations, therefore we must choose the correct method to implement it

if __name__ == '__main__':
    n = 2500
    sys.setrecursionlimit(n + 10)

    startingTime = time.time()
    factorial_1(n)
    endTime = time.time()
    print(f"Execution time with recursion\t{endTime - startingTime}");

    startingTime = time.time()
    factorial(n)
    endTime = time.time()
    print(f"Execution time with loop\t{endTime - startingTime}");

    
