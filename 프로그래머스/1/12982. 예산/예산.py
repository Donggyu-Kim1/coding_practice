def solution(d, budget):
    pay = 0
    count = 0
    d_list = sorted(d)
    for i in d_list:
        pay += i
        if pay <= budget:
            count += 1
        else:
            break
    return count