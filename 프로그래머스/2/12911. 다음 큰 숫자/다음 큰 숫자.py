def solution(n):
    new_num = n + 1
    while True:
        if bin(new_num)[2:].count("1") == bin(n)[2:].count("1"):
            return new_num
        
        new_num += 1