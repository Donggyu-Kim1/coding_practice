def solution(chicken):
    coupon = chicken
    service = 0
    
    while coupon >= 10:
        new_chicken = coupon // 10
        new_coupon = coupon % 10
        
        service += new_chicken
        coupon = new_chicken + new_coupon
    
    return service