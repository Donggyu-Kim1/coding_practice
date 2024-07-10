def solution(arr):
    answer = [-1]
    arr.remove(min(arr))
    return answer if len(arr) == 0 else arr