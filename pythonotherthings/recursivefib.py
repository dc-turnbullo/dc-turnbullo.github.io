import time

def fibonacci(n): 

    if n == 0:
        return 0
    if n == 1:
        return 1 
    return fibonacci(n-1) + fibonacci(n-2) 

def fib (n): 
    if( n == 0):
        return 0
    else:
        x = 0
        y = 1
        for i in range(1,n):
            z = (x + y)
            x = y
            y = z
            return y

for i in range(10):
    print (fib(i))






start = time.time()
#num = fibonacci(100)
num = fib(10)
end = time.time()
print(end-start)

