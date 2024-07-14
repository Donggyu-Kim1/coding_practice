from collections import defaultdict

def solution(left, right):
    a = defaultdict(list)
    answer = 0
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i % j == 0:
                a[i].append(j)
                
    
    for l, n in a.items():
        if len(n) % 2 == 0:
            answer += l
        else:
            answer -= l
        
    return answer