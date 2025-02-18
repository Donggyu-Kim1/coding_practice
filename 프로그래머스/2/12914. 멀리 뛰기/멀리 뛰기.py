def solution(n):
    
    if n < 3:
        return n
    
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    for k in range(3, n+1):
        dp[k] = (dp[k-1] + dp[k-2]) % 1234567
        
    return dp[n]