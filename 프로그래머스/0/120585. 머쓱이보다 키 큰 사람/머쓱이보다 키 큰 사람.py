def solution(array, height):
    arr = list(array)
    arr.append(height)
    arr1 = sorted(arr, reverse=True)
    result = arr1.index(height)
    return result