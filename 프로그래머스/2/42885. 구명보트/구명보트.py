def solution(people, limit):
    boat = 0
    people.sort()
    left = 0
    right = len(people) - 1
    
    while left <= right:
        if left == right:
            boat += 1
            break
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        boat += 1
            
    return boat
    
    