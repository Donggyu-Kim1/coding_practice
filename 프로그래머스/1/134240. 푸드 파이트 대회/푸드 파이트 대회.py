def solution(food):
    answer = ''
    food_number = 0
    
    for i in food[1:]:
        food_number += 1
        if i % 2 == 0:
            answer += str(food_number) * int(i / 2)
        else:
            answer += str(food_number) * int((i - 1) / 2)
        
    answer += "0"

    for i in food[:0:-1]:
        if i % 2 == 0:
            answer += str(food_number) * int(i / 2)
        else:
            answer += str(food_number) * int((i - 1) / 2)
        
        food_number -= 1
    return answer