# 4006
# [Professional] 고속도로 건설 2

'''
모든 도로가 연결됨 => 최소신장트리
prim
1. 노드 시작
2. 인접 리스트에서 최소비용노드
3. 반복
'''

from heapq import heappush, heappop

def prim(s):
    pq = [(0,s)]
    visited = [0] * (N+1)
    # 가중치 합
    sum_w = 0
    # 반복
    while pq:
        ww, v = heappop(pq)
        if visited[v]:
            continue
        # 방문 처리
        visited[v] = 1
        sum_w += ww

        # 인접한 리스트 중 방문하지 않았다면 삽입
        for n_w, n_v in graph[v]:
            if not visited[n_v]:
                heappush(pq, (n_w, n_v))

    return sum_w


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, c = map(int, input().split())
        graph[s].append((c,e))
        graph[e].append((c,s))

    print(f'#{tc} {prim(1)}')
