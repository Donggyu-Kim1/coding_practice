def solution(dots):
    for i in range(3):
        if dots[0][0] - dots[i][0] != 0:
            len_x = abs(dots[0][0] - dots[i][0])
        if dots[0][1] - dots[i][1] != 0:
            len_y = abs(dots[0][1] - dots[i][1])
        else:
            pass
    return len_x * len_y