import heapq
import sys
input = sys.stdin.readline

info = []
def dijkstra(start):
    result = [float('inf')] * (N + 1)
    result[start] = 0
    pq = [(0, start)]

    while pq:
        price, now = heapq.heappop(pq)
        if result[now] < price: continue # price가 크다면 이미 최단시간 X -> continue

        for next_idx, next_price in MAP[now]: # now에서 갈 수 있는 경로 탐색
            price_sum = price + next_price
            if result[next_idx] > price_sum:
                result[next_idx] = price_sum # 값 갱신
                heapq.heappush(pq, (price_sum, next_idx))

    return result # start에서 각 마을로 가는데 걸리는 소요시간 리스트

N, M, X = map(int, input().split())
MAP = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split()) # 시작점, 끝점, 소요시간
    MAP[s].append((e, t)) 

max_v = float('-inf')
back = dijkstra(X) # 각 학생이 집으로 돌아오는데 걸린 소요시간
for i in range(1, N+1):
    go = dijkstra(i) # i에서 X로 가는데 걸리는 소요시간
    max_v = max(max_v, go[X] + back[i]) # X까지 가는데 걸린 시간 + i로 돌아오는데 걸린 시간

print(max_v)