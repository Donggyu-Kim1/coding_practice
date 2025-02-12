def solution(s):
    new_num = ""
    discard = 0
    count = 0
    
    while s != "1":
        for i in s:
            if i == "0":
                discard += 1
            else:
                new_num += i
        
        s = bin(len(new_num))[2:]
        new_num = ""
        count += 1
    
    return [count, discard]