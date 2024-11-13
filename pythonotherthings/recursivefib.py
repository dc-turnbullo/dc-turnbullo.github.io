import time

def fibonacci(n): 

    if n == 0:
        return 0
    if n == 1:
        return 1 
    return fibonacci(n-1) + fibonacci(n-2) 

def fib(n):
    f = []
    a = 0
    b = 1
    if n == 0 or n == 1:
        print(n)
    else:
        f.append(a)
        f.append(b)
        while len(f) != n:
            temp = a + b
            f.append(temp)
            a = b
            b = temp

    print (f)
    return f










start = time.time()
#num = fibonacci(100)
num = fib(4300)
end = time.time()
print(f"the time taken is: {end-start} seconds")
print(num[5])

