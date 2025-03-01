def solution(s, skip, index):
    answer = ''
    for alpha in s:
        new_word = ord(alpha)
        i = 0
        while i != index:
            new_word += 1
            while chr((new_word + 7) % 26 + 97) in skip:
                new_word += 1
            
            i += 1
                
        
        answer += chr((new_word + 7) % 26 + 97)
        
    return answer