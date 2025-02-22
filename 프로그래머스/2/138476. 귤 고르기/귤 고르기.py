from collections import Counter

def solution(k, tangerine):
    i = 0
    count = Counter(tangerine)
    count = sorted(list(count.values()), reverse=True)
    for value in count:
        k -= value
        i += 1
        if k <= 0:
            return i