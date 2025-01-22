def is_square_possible(park, start_i, start_j, size):
    if start_i + size > len(park) or start_j + size > len(park[0]):
        return False
    
    for i in range(start_i, start_i + size):
        for j in range(start_j, start_j + size):
            if park[i][j] != "-1":
                return False
    
    return True

def solution(mats, park):
    mats.sort(reverse=True)
    
    for size in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                if park[i][j] == "-1":
                    if is_square_possible(park, i, j, size) == True:
                        return size
    
    return -1
                    
    
                
    return dic2