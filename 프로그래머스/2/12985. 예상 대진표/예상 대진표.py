def solution(n,a,b):
    answer = 1

    while max(a, b) % 2 != 0 or abs(a - b) != 1:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1
    
    return answer