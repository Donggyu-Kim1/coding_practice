def solution(n):
    answer = 0
    measure = {}
    
    for i in range(1, n + 1):
        measure[i] = 0
        for j in range(1, n + 1):
            if i - j >= 0:
                if i % j == 0:
                    measure[i] += 1
                else:
                    pass
            else:
                pass
            
    for k in measure.keys():
        if measure[k] >= 3:
            answer += 1
    return answer