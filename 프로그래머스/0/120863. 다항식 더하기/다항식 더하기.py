def solution(polynomial):
    coefficient = 0
    constant = 0
    polynomial_list = polynomial.split(" ")
    
    for i in polynomial_list:
        if i[-1] == "x":
            if i == "x":
                coefficient += 1
            else:
                coefficient += int(i[:-1])
        elif i.isdigit() == True:
            constant += int(i)
    
    # coefficient가 1일 때와 그 외의 경우를 구분
    if coefficient == 1:
        coef_str = "x"
    elif coefficient > 1:
        coef_str = f"{coefficient}x"
    else:
        coef_str = ""
        
    if constant == 0:
        return coef_str if coef_str else "0"
    elif coefficient == 0:
        return str(constant)
    else:
        return f"{coef_str} + {constant}"