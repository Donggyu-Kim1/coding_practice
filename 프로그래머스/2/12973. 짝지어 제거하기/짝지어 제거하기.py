def solution(s):
    lis = []
    for i in s:
        lis.append(i)
    
    stack = []
    for i in lis:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        return 1
    else:
        return 0