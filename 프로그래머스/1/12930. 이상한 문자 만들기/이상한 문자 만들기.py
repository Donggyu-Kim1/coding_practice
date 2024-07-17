def solution(s):
    s = s.split(' ')
    s_list = []
    for i in s:
        s_list.append(list(i))
    
    for i in range(len(s_list)):
        for j in range(len(s_list[i])):
            if j % 2 == 0:
                s_list[i][j] = s_list[i][j].upper()
            else:
                s_list[i][j] = s_list[i][j].lower()
    
    for i in range(len(s_list)):
        s_list[i] = ''.join(s_list[i])
    
    return ' '.join(s_list)