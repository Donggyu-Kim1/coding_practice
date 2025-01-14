def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit() == False:
            my_string = my_string.replace(i, " ")
    
    my_list = my_string.split(" ")
    for i in my_list:
        if i.isdigit() == True:
            answer += int(i)
    return answer