def solution(name, yearning, photo):
    score = 0
    answer = []
    for people in photo:
        for person in people:
            if person in name:
                score += yearning[name.index(person)]
        
        answer.append(score)
        score = 0
    return answer