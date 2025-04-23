# 4007
# [Professional] 간담회 참석

'''
파티와 유사
역방향 그래프 하나 더 만들기
다익스트라
'''

from heapq import heappush, heappop

def dijkstra(lst):
    # N번 사원에 도달하는 최소 시간
    min_t = [float('inf') for _ in range(N+1)]
    pq = []
    # 시작점 삽입 (X부터 시작)
    min_t[X] = 0
    heappush(pq, (0,X))
    while pq:
        times, node = heappop(pq)
        # 현재 노드까지의 최소시간보다 더 크면 넘김
        if min_t[node] < times:
            continue

        # 인접한 노드로 이동할 때
        for next_t, next_n in lst[node]:
            # 새로 가중치 계산
            new_t = times + next_t
            # 이동하는 노드까지의 최소시간보다 작으면
            if new_t < min_t[next_n]:
                # 갱신
                min_t[next_n] = new_t
                # 큐 삽입
                heappush(pq, (new_t, next_n))

    return min_t

T = int(input())

for tc in range(1,T+1):
    N, M, X = map(int, input().split())
    # 정방향
    g = [[] for _ in range(N+1)]
    # 역방향
    g_r = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, t = map(int, input().split())
        # 가중치와 함께 저장, 가중치를 앞에 저장(우선순위)
        g[s].append((t,e))
        g_r[e].append((t,s))

    # 사원별 최소 이동 경로(시간) 리스트 가져오기
    to_x = dijkstra(g)
    from_x = dijkstra(g_r)

    max_t = 0

    # 가는 시간 + 오는 시간의 최댓값 찾기
    for i in range(1,N+1):
        max_t = max(max_t, to_x[i] + from_x[i])
    print(f'#{tc} {max_t}')