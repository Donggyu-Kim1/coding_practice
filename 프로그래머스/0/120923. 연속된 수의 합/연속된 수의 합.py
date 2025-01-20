def solution(num, total):
    start_num = int(total/num) - int(num/2)
    last_num = start_num + num
    if total % num == 0:
        return [i for i in range(start_num, last_num)]
    else:
        return [i for i in range(start_num + 1, last_num + 1)]