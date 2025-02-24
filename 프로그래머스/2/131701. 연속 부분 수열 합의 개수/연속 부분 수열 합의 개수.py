def solution(elements):
    n = len(elements)
    result_set = set()
    
    for k in range(1, n + 1):
        current_sum = sum(elements[0:k])
        result_set.add(current_sum)
        
        for i in range(1, n):
            current_sum = current_sum - elements[i-1] + elements[(i+k-1) % n]
            result_set.add(current_sum)
    
    return len(result_set)