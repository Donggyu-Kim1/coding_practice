def solution(s):
    result = sorted(str(s), reverse = True)
    return int(''.join(result))