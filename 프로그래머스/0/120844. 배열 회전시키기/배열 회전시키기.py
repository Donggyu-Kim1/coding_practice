from collections import deque

def solution(numbers, direction):
    num = deque(numbers)
    if direction == 'right':
        num.rotate(1)
    else:
        num.rotate(-1)
        
    return list(num)