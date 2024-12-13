def solution(my_string, overwrite_string, s):
    answer = ''
    count = 0
    for i in range(len(my_string)):
        if count < s:
            answer += my_string[i]
        elif count >= s and count < len(overwrite_string) + s:
            answer += overwrite_string[i - s]
        else:
            answer += my_string[i]
        count += 1
    return answer