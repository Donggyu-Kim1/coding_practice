def solution(n):
    answer = ''
    
    while n:
        answer = str(n % 3) + answer
        n //= 3
    
    return int(answer[::-1], 3)
    