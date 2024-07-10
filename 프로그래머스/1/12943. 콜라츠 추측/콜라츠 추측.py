def solution(num):
    i = 0
    if num == 1:
        return 0
    while True:
        if num % 2 == 0:
            num /= 2
            i += 1
            if num == 1:
                break
        else:
            num = (num * 3) + 1
            i += 1
            if num == 1:
                break
    
    if i > 500:
        return -1
    else:
        return i