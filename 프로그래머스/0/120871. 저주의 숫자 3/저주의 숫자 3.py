def solution(n):
    answer = {}
    for i in range(1, 101):
        answer[i] = i
    
    changed = True
    while changed:
        changed = False
        for i in range(1, 101):
            current = answer[i]
            if current % 3 == 0 or "3" in str(current):
                for j in range(i, 101):
                    answer[j] += 1
                changed = True
                break
    
    return answer[n]
                