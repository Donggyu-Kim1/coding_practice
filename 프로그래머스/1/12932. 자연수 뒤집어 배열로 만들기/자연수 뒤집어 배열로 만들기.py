def solution(n):
    a = []
    str_n = str(n)
    for i in str_n[::-1]:
        a.append(int(i))
    
    return a