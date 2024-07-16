def solution(n, m):
    min_list = []
    max_list = []
    answer = []
    for i in range(1, m+1):
        if n % i == 0 and m % i == 0:
            min_list.append(i)
            max_list.append(n/i*m/i*i)
    
    answer.append(min_list[-1])
    answer.append(max_list[-1])
    return answer