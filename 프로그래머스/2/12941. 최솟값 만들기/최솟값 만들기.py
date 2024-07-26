def solution(A, B):
    A.sort(reverse=True)  # 리스트 A를 내림차순으로 정렬
    B.sort()  # 리스트 B를 오름차순으로 정렬
    
    answer = sum(a * b for a, b in zip(A, B))  # A와 B의 원소를 곱하고 합계를 계산
    
    return answer