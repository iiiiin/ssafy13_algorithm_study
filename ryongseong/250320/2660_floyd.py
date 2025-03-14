import sys

input = sys.stdin.readline
INF = float("inf")


def floyd(graph):
    n = len(graph)
    for i in range(n):
        for r in range(n):
            for c in range(r + 1, n):
                graph[r][c] = min(graph[r][c], graph[r][i] + graph[i][c])
                graph[c][r] = graph[r][c]


N = int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

floyd(graph)

min_score = INF
result = []

for i in range(1, N + 1):
    graph[i][i] = 0
    score = max(graph[i][1:])
    if score < min_score:
        min_score = score
        result = [i]
    elif score == min_score:
        result.append(i)

print(min_score, len(result))
print(*sorted(result))
