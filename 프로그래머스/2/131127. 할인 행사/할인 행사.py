from collections import Counter

def solution(want, number, discount):
    answer = 0
    n = len(want)
    total = sum(number)
    wish_list = {}
    for i in range(n):
        wish_list[want[i]] = number[i]
    
    wish_list = sorted(wish_list.items(), key = lambda item: item[0])
        
    days = len(discount)
    for i in range(days - total + 1):
        discount_list = sorted(Counter(discount[i:i+total]).items(), key = lambda item: item[0])
        if discount_list == wish_list:
            answer += 1
    
    return answer