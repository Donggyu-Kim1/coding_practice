def solution(quiz):
    answer = []
    split_quiz = []
    for i in quiz:
        split_quiz.append(i.split(" "))
    
    for i in split_quiz:
        if i[1] == "+":
            if int(i[0]) + int(i[2]) == int(i[-1]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(i[0]) - int(i[2]) == int(i[-1]):
                answer.append("O")
            else:
                answer.append("X")
    return answer