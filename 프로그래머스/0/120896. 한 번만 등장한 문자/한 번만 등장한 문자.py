from collections import Counter

def solution(s):
    dic = Counter(s)
    
    answer = ''
    for k, v in dic.items():
        if v == 1:
            answer += k
            
    return ''.join(sorted(answer))