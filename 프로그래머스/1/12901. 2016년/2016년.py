def solution(a, b):
    answer = ''
    day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    if a == 1:
        return day[(b % 7 + 4) % 7] # 막날이 일요일
    elif a == 2:
        return day[b % 7] # 막날이 월요일
    elif a == 3:
        return day[(b % 7 + 1) % 7] # 막날이 목요일
    elif a == 4:
        return day[(b % 7 + 4) % 7] # 막날이 토요일
    elif a == 5:
        return day[(b % 7 + 6) % 7] # 막날이 화요일
    elif a == 6:
        return day[(b % 7 + 2) % 7] # 막날이 목요일
    elif a == 7:
        return day[(b % 7 + 4) % 7] # 막날이 일요일
    elif a == 8:
        return day[b % 7] # 막날이 수요일
    elif a == 9:
        return day[(b % 7 + 3) % 7] # 막날이 금요일
    elif a == 10:
        return day[(b % 7 + 5) % 7] # 막날이 월요일
    elif a == 11:
        return day[(b % 7 + 1) % 7] # 막날이 수요일
    else:
        return day[(b % 7 + 3) % 7]
    
        