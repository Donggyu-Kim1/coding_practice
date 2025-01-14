from itertools import permutations

def solution(numbers):
    cards = list(permutations(numbers, 2))
    answer = []
    
    for i in cards:
        answer.append(i[0] * i[1])
    return max(answer)