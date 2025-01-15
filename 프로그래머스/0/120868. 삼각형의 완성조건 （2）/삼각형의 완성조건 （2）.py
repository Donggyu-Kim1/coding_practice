def solution(sides):
    answer = []
    for x in range(sides[0] + sides[1]):
        if x > max(sides) and x < sides[0] + sides[1]:
            answer.append(x)
        elif max(sides) < x + min(sides):
            answer.append(x)
        
    return len(answer)