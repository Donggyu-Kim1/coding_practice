def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit() == True:
            answer.append(int(i))
            
    sorted_answer = sorted(answer)
    return sorted_answer