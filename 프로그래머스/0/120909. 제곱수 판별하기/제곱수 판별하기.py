def solution(n):
    answer = 0
    if int(n ** 0.5) == n ** 0.5:
        return 1
    else:
        return 2