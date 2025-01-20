def solution(before, after):
    answer = 0
    before_list = []
    after_list = []
    for i in before:
        before_list.append(i)
    
    before_list = sorted(before_list)
    
    for i in after:
        after_list.append(i)
        
    after_list = sorted(after_list)
    
    if before_list == after_list:
        return 1
    else:
        return 0