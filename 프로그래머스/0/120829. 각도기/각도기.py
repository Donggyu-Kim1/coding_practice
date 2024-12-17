def solution(angle):
    case = {"acute" : 1,
            "right" : 2,
            "obtuse" : 3,
            "straight": 4
           }
    if angle < 90:
        return case["acute"]
    elif angle == 90:
        return case["right"]
    elif angle < 180:
        return case["obtuse"]
    else:
        return case["straight"]