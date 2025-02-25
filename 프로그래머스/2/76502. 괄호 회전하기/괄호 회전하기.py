def solution(s):
    count = 0
    n = len(s)

    for i in range(n):
        rotated = s[i:] + s[:i]
        stack = []
        valid = True

        for char in rotated:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    valid = False
                    break
                last = stack.pop()
                if (char == ")" and last != "(") or \
                   (char == "}" and last != "{") or \
                   (char == "]" and last != "["):
                    valid = False
                    break
        
        if valid and not stack:
            count += 1

    return count