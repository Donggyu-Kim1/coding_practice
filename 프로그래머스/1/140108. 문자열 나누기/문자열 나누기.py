def solution(s):
    answer = 0
    count = 0
    count_2 = 0
    x = ''  # 현재 기준 문자

    for i in s:
        if count == 0:
            x = i
        
        if i == x:
            count += 1
        else:
            count_2 += 1

        if count == count_2:
            answer += 1
            count, count_2 = 0, 0

    if count != 0 or count_2 != 0:
        answer += 1

    return answer
