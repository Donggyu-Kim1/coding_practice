def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i

def solution(arr):
    a, b = arr[0], arr[1]
    for k in range(2, len(arr)):
        a, b = lcm(a, b), arr[k]
        
    return lcm(a, b)