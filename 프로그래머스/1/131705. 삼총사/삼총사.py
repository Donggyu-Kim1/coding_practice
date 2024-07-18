from itertools import combinations

def solution(number):
    # 리스트에서 3개 뽑기
    sam_chong_sa = list(combinations(number, 3))
    
    result = 0
    for i in sam_chong_sa:
        if sum(i) == 0:
            result += 1
    return result