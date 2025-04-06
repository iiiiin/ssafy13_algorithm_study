import heapq

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    dist = [[float("inf")] * N for _ in range(N)]
    dist[0][0] = 0

    queue = [(0, 0, 0)]

    while queue:
        cost, r, c = heapq.heappop(queue)

        if cost > dist[r][c]:
            continue

        if (r, c) == (N - 1, N - 1):
            break

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cost + matrix[nr][nc]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(queue, (new_cost, nr, nc))

    print(f"#{test_case} {dist[-1][-1]}")
