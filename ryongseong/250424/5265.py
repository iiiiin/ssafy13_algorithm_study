def tsp(visited, cur):
    if visited == (1 << N) - 1:
        return matrix[cur][0] if matrix[cur][0] > 0 else float("inf")

    if dp[visited][cur] != -1:
        return dp[visited][cur]

    min_cost = float("inf")

    for next in range(N):
        if not (visited & (1 << next)) and matrix[cur][next] > 0:
            min_cost = min(
                min_cost, matrix[cur][next] + tsp(visited | (1 << next), next)
            )

    dp[visited][cur] = min_cost
    return min_cost


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dp = [[-1] * N for _ in range(1 << N)]
    result = tsp(1, 0)
    print(f"#{test_case} {result}")
