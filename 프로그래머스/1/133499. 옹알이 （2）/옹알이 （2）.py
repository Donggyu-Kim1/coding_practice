import re

def solution(babbling):
    count = 0
    pattern = re.compile(r"^(aya|ye|woo|ma)+$")
    repeat_check = re.compile(r"(aya|ye|woo|ma)\1")
    
    for text in babbling:
        if pattern.fullmatch(text) and not repeat_check.search(text):
            count += 1
            
    return count
            