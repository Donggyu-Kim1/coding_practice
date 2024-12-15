def solution(array):
    answer = {}
    for i in array:
        if i not in answer:
            answer[i] = 1
        else:
            answer[i] += 1
    
    answer1 = []
    max_value = max(answer.values())
    for k, v in answer.items():
        if v == max_value:
            answer1.append(k)
            
    if len(answer1) == 1:
        return answer1[0]
    else:
        return -1