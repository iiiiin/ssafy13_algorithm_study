import heapq

INF = int(1e9)


def dijkstra(start, graph):
    pq = [(0, start)]
    dists = [INF] * (N + 1)
    dists[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if dists[now] < dist:
            continue

        for next_dist, next_node in graph[now]:
            if dists[next_node] > dist + next_dist:
                dists[next_node] = dist + next_dist
                heapq.heappush(pq, (dist + next_dist, next_node))

    return dists


T = int(input())

for test_case in range(1, T + 1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    reverse_graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        s, e, t = map(int, input().split())
        graph[s].append((t, e))
        reverse_graph[e].append((t, s))

    to_X = dijkstra(X, reverse_graph)
    from_X = dijkstra(X, graph)

    max_time = 0
    for i in range(1, N + 1):
        total_time = to_X[i] + from_X[i]
        if total_time < INF:
            max_time = max(max_time, total_time)

    print(f"#{test_case} {max_time}")
