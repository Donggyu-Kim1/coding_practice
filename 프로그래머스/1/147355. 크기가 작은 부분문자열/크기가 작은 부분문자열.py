def solution(t, p):
    part_list = []
    answer = 0
    for i in range(len(t)-len(p)+1):
        part_list.append(t[i:i+len(p)])
        
    int_list = list(map(int, part_list))
    for i in  int_list:
        if int(p) >= i:
            answer += 1
    return answer