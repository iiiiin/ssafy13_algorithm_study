from heapq import heappop, heappush
import sys

input = sys.stdin.readline

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = int(1e9)


def dijkstra():
    dists = [[INF] * N for _ in range(N)]
    pq = [(matrix[0][0], 0, 0)]
    dists[0][0] = 0

    while pq:
        cost, r, c = heappop(pq)

        if (r, c) == (N - 1, N - 1):
            return dists[r][c]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cost + matrix[nr][nc]

                if new_cost < dists[nr][nc]:
                    dists[nr][nc] = new_cost
                    heappush(pq, (new_cost, nr, nc))


tc = 0
while True:
    N = int(input())
    if N == 0:
        break

    matrix = [list(map(int, input().split())) for _ in range(N)]

    tc += 1
    print(f"Problem {tc}: {dijkstra()}")
