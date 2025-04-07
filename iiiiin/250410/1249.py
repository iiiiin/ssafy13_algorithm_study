# 1249.
# [S/W 문제해결 응용] 4일차 - 보급로

'''
최단 경로 => 다익스트라
인접리스트가 아닌 상하좌우 이동의 경우에서 탐색
'''

from heapq import heappush, heappop


def dijkstra(lst):
    # 배열 위치별 최소 가중치
    min_w = [[float('inf')] * N for _ in range(N)]
    pq = []
    # 시작점 처리: 시작점에서 시작점까지 이동하는 데 최소 가중치 0
    min_w[0][0] = 0
    # 우선순위 큐에 삽입 (가중치, 행, 열)
    heappush(pq, (0, 0, 0))

    while pq:
        w, r, c = heappop(pq)

        # (r,c)까지 이동하는 데 드는 복구시간(가중치)가
        # 이전 최솟값보다 크면, 계산 안함
        if min_w[r][c] < w:
            continue

        # 상하좌우 탐색
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            # 범위 확인
            if 0 <= nr < N and 0 <= nc < N:
                # (nr,nc)까지 이동하는 데 드는 복구시간 계산
                nt = min_w[r][c] + lst[nr][nc]
                # 이전 최소값보다 작다면 갱신
                if nt < min_w[nr][nc]:
                    min_w[nr][nc] = nt
                    heappush(pq, (min_w[nr][nc], nr, nc))

    return min_w[N - 1][N - 1]


T = int(input())

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = dijkstra(arr)
    print(f'#{tc} {result}')