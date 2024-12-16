def solution(n):
    count = 1
    for i in range(6 * n):
        if (count * n) % 6 == 0:
            return (count * n) // 6
        else:
            count += 1