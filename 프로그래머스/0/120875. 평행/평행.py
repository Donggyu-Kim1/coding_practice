from decimal import Decimal

def solution(dots):
    answer = 0
    if Decimal(dots[0][0] - dots[2][0])/(dots[0][1] - dots[2][1]) == Decimal(dots[1][0] - dots[3][0])/(dots[1][1] - dots[3][1]):
        return 1
    elif Decimal(dots[0][0] - dots[1][0])/(dots[0][1] - dots[1][1]) == Decimal(dots[2][0] - dots[3][0])/(dots[2][1] - dots[3][1]):
        return 1
    else:
        return 0