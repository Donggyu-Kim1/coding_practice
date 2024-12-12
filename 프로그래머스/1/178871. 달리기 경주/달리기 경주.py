def solution(players, callings):
    name_score = {}
    score_name = {}
    for i in range(len(players)):
        name_score[players[i]] = i
        score_name[i] = players[i]
    
    for i in range(len(callings)):
        curr_idx = name_score[callings[i]]  # 현재 선수의 등수
        prev_idx = curr_idx - 1  # 앞 선수의 등수
        
        # 앞 선수의 이름
        overtaken_player = score_name[prev_idx]
        
        # 두 선수의 등수 교체
        name_score[callings[i]] = prev_idx
        name_score[overtaken_player] = curr_idx
        
        # score_name도 교체
        score_name[prev_idx] = callings[i]
        score_name[curr_idx] = overtaken_player
    
    # 1등부터 순서대로 이름을 배열에 담아 반환
    return [score_name[i] for i in range(len(players))]
            