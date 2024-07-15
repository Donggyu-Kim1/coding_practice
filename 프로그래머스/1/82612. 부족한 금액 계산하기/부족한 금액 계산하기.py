def solution(price, money, count):
    total = 0
    for i in range(count+1):
        total += i
    
    total_price = price * total
    if total_price >= money:
        return total_price-money
    else:
        return 0