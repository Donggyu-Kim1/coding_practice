def solution(numbers):
    num_list = []
    for i in range(10):
        num_list.append(i)
    
    answer = 0
    for j in num_list:
        if j not in numbers:
            answer += j
    
    return answer