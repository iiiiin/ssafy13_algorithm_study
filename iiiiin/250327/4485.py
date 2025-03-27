# 4485
# 녹색 옷 입은 애가 젤다지?

'''
[0][0] -> [N-1][N-1] 까지 이동
상하좌우 탐색 (델타 탐색)
각 칸을 탐색하면서 도착점까지의 최소금액(최단경로) 구하기
다익스트라
=> 방문리스트(배열) 필요 X, 현재 우선순위큐에서 꺼낸 가중치가 꺼낸 노드까지의 저장된 가중치보다 작으면 갱신, 크면 continue
'''

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(sx, sy):
    # 각 위치별 최소 가중치 배열
    min_loss = [[float('inf')] * N for _ in range(N)]
    # 시작점 힙큐 삽입, 최소 가중치 갱신
    pq = [(cave[sx][sy], sx, sy)]
    min_loss[sx][sy] = cave[sx][sy]
    # 큐 비어있지 않을 때까지
    while pq:
        # 일단 꺼내기
        w, x, y = heappop(pq)
        # 현재 노드까지의 가중치 보다 크면 pass
        if w > min_loss[x][y]:
            continue
        # 델타 탐색으로 이동했을 때의 최소를 확인
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            # 인덱스 범위 확인
            if 0 <= nx < N and 0 <= ny < N:
                nw = w + cave[nx][ny]
                # 이동할 노드에 저장된 가중치보다 작을 때 갱신, 힙큐 삽입
                if nw < min_loss[nx][ny]:
                    min_loss[nx][ny] = nw
                    heappush(pq, (nw, nx, ny))

    # 모든 반복을 수행 후 도착점에 저장된 최소금액 반환
    return min_loss[N - 1][N - 1]


i = 1
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while True:
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    result = dijkstra(0,0)
    print(f'Problem {i}: {result}')
    i += 1
