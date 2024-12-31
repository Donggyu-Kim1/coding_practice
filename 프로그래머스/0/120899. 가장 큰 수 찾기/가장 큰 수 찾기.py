def solution(array):
    answer = []
    max_array = max(array)
    answer.append(max_array)
    answer.append(array.index(max_array))
    return answer