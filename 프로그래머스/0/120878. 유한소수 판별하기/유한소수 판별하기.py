def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(a, b):
    gcd = get_gcd(a, b)
    b //= gcd

    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5

    return 1 if b == 1 else 2