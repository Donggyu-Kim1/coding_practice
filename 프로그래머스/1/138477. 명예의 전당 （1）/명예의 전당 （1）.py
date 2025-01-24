def solution(k, score):
    answer = []
    result = []
    for i in score:
        answer.append(i)
        answer.sort(reverse=False)
        if len(answer) > k:
            del(answer[0])

        result.append(min(answer))
    return result