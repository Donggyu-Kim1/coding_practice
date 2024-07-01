def solution(survey, choices):
    # 1. 성격별 점수 딕셔너리 초기화
    scores = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    
    # 2. 입력받은 survey와 choices를 기반으로 점수 합산
    for s, choice in zip(survey, choices):
        if choice < 4:
            scores[s[0]] += 4 - choice
        elif choice > 4:
            scores[s[1]] += choice - 4
    
    # 3. 각 지표에서 더 높은 점수를 받은 성격 유형 결정
    result = []
    result.append('R' if scores['R'] >= scores['T'] else 'T')
    result.append('C' if scores['C'] >= scores['F'] else 'F')
    result.append('J' if scores['J'] >= scores['M'] else 'M')
    result.append('A' if scores['A'] >= scores['N'] else 'N')
    
    # 4. 결과를 문자열로 변환하여 반환
    return ''.join(result)