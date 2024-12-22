def solution(my_string):
    answer = ''
    모음 = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i not in 모음:
            answer += i
    return answer