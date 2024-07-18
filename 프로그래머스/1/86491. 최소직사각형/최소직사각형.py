def solution(sizes):
    line_x = []
    line_y = []
    for i in range(len(sizes)):
        line_x.append(max(sizes[i]))
        line_y.append(min(sizes[i]))
    
    return max(line_x) * max(line_y)