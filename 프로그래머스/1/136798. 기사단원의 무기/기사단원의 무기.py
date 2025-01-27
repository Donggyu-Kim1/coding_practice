def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        count = 0
        for l in range(1, int((i)**0.5)+1):
            if i % l == 0:
                count += 1
                if i != (i//l)**2:
                    count += 1
        
        if count > limit:
            answer += power
        else:
            answer += count
    
    return answer