def solution(score):
    scores_with_idx = []
    for idx, [eng, math] in enumerate(score):
        avg = (eng + math) / 2
        scores_with_idx.append([avg, idx])
    
    sorted_scores = sorted(scores_with_idx, key=lambda x: -x[0])
    
    ranks = [0] * len(score)
    rank = 1
    
    for i in range(len(score)):
        if i > 0 and sorted_scores[i][0] != sorted_scores[i-1][0]:
            rank = i + 1
    
        idx = sorted_scores[i][1]
        ranks[idx] = rank         
    return ranks