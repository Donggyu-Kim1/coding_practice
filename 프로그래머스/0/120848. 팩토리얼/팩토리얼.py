def factorial(x):
    k = 1
    for i in range(1, x + 1):
        k *= i
    
    return k

def solution(n):
    x_list = []
    x = 1
    while n - factorial(x) >= 0:
        x_list.append(x)
        x += 1
    return max(x_list)