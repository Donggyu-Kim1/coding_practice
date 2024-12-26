def solution(array, n):
    answer = {}
    for i in array:
        answer[i] = abs(n - i)
    
    min_values = min(answer.values())
    min_keys = []
    
    for k, v in answer.items():
        if v == min_values:
            min_keys.append(k)
    
    return min(min_keys)