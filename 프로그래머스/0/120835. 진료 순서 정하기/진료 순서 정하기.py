def solution(emergency):
    answer = {}
    result = []
    sorted_emergency = sorted(emergency)[::-1]
    
    for i in range(len(sorted_emergency)):
        answer[sorted_emergency[i]] = i + 1
    
    for i in emergency:
        result.append(answer[i])
    
    return result