def factorial_iter(n):
    result = 1
    for k in range(2, n+1):
        result *= k
            
    return result

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
c = int(input("팩토리얼 계산: "))
print(factorial(c))