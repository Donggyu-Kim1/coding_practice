import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    count = 0

    while len(scoville) > 1 and scoville[0] < K:
        new_sco = hq.heappop(scoville) + hq.heappop(scoville) * 2
        hq.heappush(scoville, new_sco)
        count += 1

    return count if scoville[0] >= K else -1
