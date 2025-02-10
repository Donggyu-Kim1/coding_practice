from collections import Counter

def solution(N, stages):
    challenger_count = Counter(stages)
    failure_rates = {}
    total_players = len(stages)
    
    for stage in range(1, N+1):
        if total_players > 0:
            failure_rate = challenger_count[stage] / total_players
            total_players -= challenger_count[stage]
        else:
            failure_rate = 0
        
        failure_rates[stage] = failure_rate
    
    result = sorted(failure_rates, key=lambda x: (-failure_rates[x], x))
        
    return result