def solution(s, n):
    result = ''
    for i in s:
        if ' ' == i:
            result += ' '
        elif i.islower():
            result += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        elif i.isupper():
            result += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        else:
            result += i
    return result