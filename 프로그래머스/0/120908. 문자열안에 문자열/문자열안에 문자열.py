def solution(str1, str2):
    answer = 0
    i = 0
    while str1[i:i+len(str2)] != str2:
        i += 1
        if i > len(str1):
            return 2
    return 1