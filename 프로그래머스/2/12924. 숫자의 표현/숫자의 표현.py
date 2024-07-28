def solution(n):
    """
    자연수 n을 연속된 자연수들의 합으로 표현하는 방법의 수를 계산하는 함수입니다.

    Args:
        n (int): 자연수

    Returns:
        int: 방법의 수
    """
    ans = 0
    for i in range(1, n // 2 + 1):
        total = 0
        for j in range(i, n):
            total += j
            if total == n:
                ans += 1
            elif total > n:
                break
    return ans + 1