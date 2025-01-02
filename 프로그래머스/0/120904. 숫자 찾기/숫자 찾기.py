def solution(num, k):
    answer = 0
    i = 0
    str_num = str(num)
    try:
        while str(k) != str_num[i]:
            i += 1
        
        return str_num.index(str_num[i]) + 1
    except:
        return -1
    
    

