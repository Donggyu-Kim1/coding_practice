import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while len(scoville) > 1 and scoville[0] < K:
        new_sco = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new_sco)
        count += 1

    return count if scoville[0] >= K else -1
