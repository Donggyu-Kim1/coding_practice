def solution(id_pw, db):
    answer = ''
    i = 0
    while i != len(db):
        if id_pw[0] != db[i][0]:
            answer += "fail"
        elif id_pw[0] == db[i][0] and id_pw[1] != db[i][1]:
            answer += "wrong pw"
        else:
            answer += "login"
        i += 1
    
    if "login" in answer:
        return "login"
    elif "wrong pw" in answer:
        return "wrong pw"
    else:
        return "fail"