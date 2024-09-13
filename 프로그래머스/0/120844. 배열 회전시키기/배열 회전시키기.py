def solution(numbers, direction):
    answer = []
    if direction == 'right':
        return [numbers.pop()] + numbers
    else:
        value = numbers.pop(0)
        return numbers + [value]