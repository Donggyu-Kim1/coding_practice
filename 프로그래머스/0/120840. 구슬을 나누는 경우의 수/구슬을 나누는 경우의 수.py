def solution(balls, share):
    balls_pac = 1
    share_pac = 1
    minus_pac = 1
    for i in range(1, balls + 1):
        balls_pac *= i
    
    for i in range(1, share + 1):
        share_pac *= i
    
    for i in range(1, balls - share + 1):
        minus_pac *= i
        
    answer = balls_pac / (minus_pac * share_pac)
    
    return answer