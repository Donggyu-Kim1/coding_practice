def solution(spell, dic):
    sorted_dic = []
    
    for i in dic:
        sorted_dic.append(''.join(sorted(i)))
    
    sorted_spell = ''.join(sorted(spell))
    
    if sorted_spell in sorted_dic:
        return 1
    else:
        return 2
                