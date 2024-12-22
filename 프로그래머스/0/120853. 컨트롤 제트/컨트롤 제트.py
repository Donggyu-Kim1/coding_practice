def solution(s):
    answer = 0
    s = s.split(" ")
    for i in range(len(s)-1):
        if s[i+1] != "Z" and s[i] != "Z":
            answer += int(s[i])
        
    if s[-1] != "Z":
        answer += int(s[-1])
    
    return answer