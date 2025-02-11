def to_jaden_case(s):
    result = []
    word = ""
    c = []
    
    for a in s:
        if a.isalnum() == True:
            word += a
        elif a == " ":
            if word:
                result.append(word)
            result.append(" ")
            word = ""
        
    if word:
        result.append(word)
    
    for i in result:
        if i == " ":
            c.append(" ")
        elif len(i) > 0:
            if i[0].isdigit():
                c.append(i.lower())
            else:
                c.append(i.capitalize())
            
    return "".join(c)

def solution(s):
    return to_jaden_case(s)