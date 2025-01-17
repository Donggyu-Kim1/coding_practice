def solution(numlist, n):
    answer = []
    dis = []
    
    for i in numlist:
        dis.append(abs(n - i))
    
    dis = sorted(dis)
    re_numlist = sorted(numlist)[::-1]
    for l in dis:
        for k in re_numlist:
            if abs(n - k) == l:
                answer.append(k)
            else:
                dis = dis[1:]
    
    answer2 = []
    for i in answer:
        if i not in answer2:
            answer2.append(i)
    
    return answer2