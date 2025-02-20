def solution(n, words):
    answer = []
    word_list = []
    
    for i in range(len(words)):
        if len(words[i]) == 1:
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            return answer
        else:
            word_list.append(words[i])
            if len(word_list) > 1:
                if word_list[-2][-1] != word_list[-1][0] or word_list[-1] in word_list[:-1]:
                    answer.append(i % n + 1)
                    answer.append(i // n + 1)
                    return answer
    
    if len(answer) == 0:
        return [0, 0]