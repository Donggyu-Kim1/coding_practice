def solution(n, m, section):
    count = 0
    i = 0

    while i < len(section):
        start = section[i]
        end = start + m - 1

        i += 1
        while i < len(section) and section[i] <= end:
            i += 1

        count += 1

    return count
