def solution(brown, yellow):
    answer = []
    can_divide = []
    total_tile = brown + yellow
    
    for width in range(total_tile, 2, -1):
        if total_tile % width != 0:
            continue
            
        height = total_tile // width
    
        if (width * 2 + height * 2 - 4) == brown and (width - 2) * (height - 2) == yellow:
            return [width, height]