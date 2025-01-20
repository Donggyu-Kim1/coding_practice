def solution(A, B):
    answer = []
    i = 0
    while i != len(A):
        if B == A[-i:] + A[:-i]:
            return i
        
        i += 1
    if i == len(A):
        return -1