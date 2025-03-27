# 1774
# 우주신과의 교감

'''
우주신과 황선자씨를 최단거리의 통로로 연결
그런데? 우주신과 황선자씨가 일부 연결되어 있음
원래 처음부터 모든 노드를 연결해서 MST를 만드는 Prim에서
1. 이미 연결되어 있는 노드는 가중치 0 처리
2. 그를 제외한 모든 노드가 아닌, 인접 리스트 형태를 활용하여,
    이동할 수 있는 노드에 대해서만 탐색 수행
'''

from heapq import heappush, heappop, heapify
import sys
input = sys.stdin.readline

def prim(start):
    min_route = 0
    # 방문 리스트
    MST = [0]*(N+1)
    pq = [(0, start)]
    while pq:
        w, node = heappop(pq)
        # 방문 확인 1
        if MST[node]:
            continue
        # 방문 처리
        MST[node] = 1
        # 누적합 추각
        min_route += w

        # 해당 노드의 인접리스트에 대해 탐색
        for info in linked[node]:
            # 방문 확인 필요 X, 각 연결되어 있지 않은 인접 노드들만 힙큐에 삽입
            # 그리고 힙큐에서 꺼낼 때 이미 방문 확인
            # info => (weight, node)
            if MST[info[1]]:
                continue
            heappush(pq, info)

    return min_route

N, M = map(int, input().split())
nodes = [0] + [tuple(map(int, input().split())) for _ in range(N)]
# 인접 리스트 (우주신들의 좌표 번호는 1부터 N번)
linked = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    linked[a].append((0,b))
    linked[b].append((0,a))

# 연결되지 않은 노드에 대해 가중치 계산 수행
for i in range(1, N+1):
    for j in range(1, N+1):
        if i != j or not linked[i] or not linked[j]:
            x1, y1 = nodes[i]
            x2, y2 = nodes[j]

            weight = ((x2-x1)**2 + (y2-y1)**2)**0.5
            linked[i].append((weight, j))
# Prim 실행 (1번 노드부터 시작)
result = prim(1)
print(format(result, '.2f'))
