def solution(n):
    answer = set()
    d = 2
    
    while d <= n:
        if n % d == 0:
            answer.add(d)
            n = n // d
        else:
            d += 1
            
    return sorted(list(answer))