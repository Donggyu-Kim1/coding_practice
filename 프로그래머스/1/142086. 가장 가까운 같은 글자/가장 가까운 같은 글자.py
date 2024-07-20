def solution(s):
    ns = ''
    answer = []
    for i in range(len(s)):
        if s[i] not in ns:
            ns += s[i]
            answer.append(-1)
        else:
            answer.append(i - ns.rindex(s[i]))
            ns += s[i]
    return answer