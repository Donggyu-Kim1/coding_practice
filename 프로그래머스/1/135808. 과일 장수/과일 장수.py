def solution(k, m, score):
    answer = []
    
    # 내림차순 정렬 후 m개 추출
    sorted_score = sorted(score)[::-1]
    if len(sorted_score) % m != 0:
        sorted_score = sorted_score[0:len(sorted_score) // m * m]
        
    for i in range(0, len(sorted_score), m):
        answer.append(sorted_score[i:i+m])
    
    result = 0
    for i in answer:
        result += (min(i) * m)
    return result