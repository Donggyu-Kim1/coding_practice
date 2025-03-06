def solution(prices):
    stack = []
    seconds = 0
    n = len(prices)
    answer = [0] * n
    
    for i in range(n):
        while stack and prices[i] < prices[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx
            
        stack.append(i)
        
    while stack:
        idx = stack.pop()
        answer[idx] = n - 1 - idx
        
    return answer