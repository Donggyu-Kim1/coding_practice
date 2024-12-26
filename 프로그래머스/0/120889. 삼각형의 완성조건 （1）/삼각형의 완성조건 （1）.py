def solution(sides):
    answer = 0
    sides = sorted(sides)
    if sides[-1] - (sides[0] + sides[1])< 0:
        return 1
    else:
        return 2