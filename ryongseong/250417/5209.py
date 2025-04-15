def dfs(r, cost):
    global min_cost

    if cost >= min_cost:
        return

    if r == N:
        min_cost = min(min_cost, cost)
        return

    for c in range(N):
        if not visited[c]:
            visited[c] = 1
            dfs(r + 1, cost + matrix[r][c])
            visited[c] = 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_cost = float('inf')
    visited = [0] * N
    dfs(0, 0)
    print(f"#{test_case} {min_cost}")
