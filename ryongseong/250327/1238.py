import sys
import heapq

input = sys.stdin.readline


def dijkstra(start):
    queue = []
    distance = [float("inf") for _ in range(N + 1)]

    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for idx, c in graph[now]:
            cost = dist + c

            if distance[idx] > cost:
                distance[idx] = cost
                heapq.heappush(queue, (cost, idx))

    return distance


N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

result = float("-inf")
for i in range(1, N + 1):
    a = dijkstra(i)
    b = dijkstra(X)
    result = max(result, a[X] + b[i])

print(result)
