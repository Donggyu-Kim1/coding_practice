import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    i = math.gcd(numer, denom)
    num = numer / i
    den = denom / i
    
    answer.append(num)
    answer.append(den)
    
    return answer