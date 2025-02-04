from itertools import combinations as c

def prime_number(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True

def solution(nums):
    answer = 0
    for i in list(c(nums, 3)):
        n = sum(i)
        if prime_number(n) == True:
            answer += 1
    return answer