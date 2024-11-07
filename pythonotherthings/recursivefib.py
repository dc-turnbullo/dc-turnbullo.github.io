import time
'''
def fibonacci(n): 

    if n == 0:
        return 0
    if n == 1:
        return 1 
    return fibonacci(n-1) + fibonacci(n-2) 
'''

def fibonacci2(n): 
    fibNumbers = [0,1]   
    for i in range(2, n+1): 
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2]) 
        return fibNumbers[n]  

start = time.time()
num = fibonacci2(10)
end = time.time()
print(end-start)

