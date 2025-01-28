def solution(answers):
    supo_1 = [1, 2, 3, 4, 5]
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    supo_1_score, supo_2_score, supo_3_score = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == supo_1[i % len(supo_1)]:
            supo_1_score += 1
        
        if answers[i] == supo_2[i % len(supo_2)]:
            supo_2_score += 1
        
        if answers[i] == supo_3[i % len(supo_3)]:
            supo_3_score += 1
            
    answer = []
    if max(supo_1_score, supo_2_score, supo_3_score) == supo_1_score:
        answer.append(1)
    
    if max(supo_1_score, supo_2_score, supo_3_score) == supo_2_score:
        answer.append(2)
    
    if max(supo_1_score, supo_2_score, supo_3_score) == supo_3_score:
        answer.append(3) 
    
    return answer