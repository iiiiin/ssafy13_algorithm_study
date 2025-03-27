# 1238
# 파티

'''
다익스트라
X에서 출발하는 다익스트라
단방향 그래프의 가중치(시간) 뒤집기
1. 우선순위큐(힙큐)로 최소가중치 가져오기
2. 현재 노드까지의 최단경로로 저장된 가중치보다 가져온 값이 크면 continue
3. 모든 노드에 대해 탐색
4. 다음 노드와 함께 누적 가중치 계산
5. 다음 노드에 저장된 가중치와 계산한 누적 가중치 비교
6. 노드(인덱스)별 최소 가중치 반환
'''

from heapq import heappush, heappop
import sys

input = sys.stdin.readline

def dijkstra(lst):
    # 최소 가중치 저장 리스트
    min_time = [float('inf') for _ in range(N+1)]
    # 우선순위 큐
    pq = []
    # 시작점 삽입
    min_time[X] = 0
    heappush(pq, (0, X))
    while pq:
        times, node = heappop(pq)
        if min_time[node] < times:
            continue

        for next_t, next_n in lst[node]:
            new_t = min_time[node] + next_t

            if new_t < min_time[next_n]:
                min_time[next_n] = new_t
                heappush(pq, (min_time[next_n], next_n))

    return min_time

N, M, X = map(int, input().split())

# 가는 방향 그래프, 오는 방향 그래프
g = [[] for _ in range(N+1)]
g_r = [[] for _ in range(N+1)]

for _ in range(M):
    s,e,t = map(int, input().split())
    g[s].append((t,e))
    g_r[e].append((t,s))

to_x = dijkstra(g)
from_x = dijkstra(g_r)

max_t = 0
for i in range(1, N+1):
    max_t = max(max_t, to_x[i] + from_x[i])

print(max_t)
