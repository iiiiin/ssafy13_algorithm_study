def dfs(node, visited, graph):
    max_length = 1
    for neighbor in graph[node]:
        if neighbor not in visited:
            max_length = max(max_length, 1 + dfs(neighbor,
                             visited | {neighbor}, graph))
    return max_length


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    graph = {i: set() for i in range(1, N + 1)}
    for _ in range(K):
        data = list(map(int, input().split()))
        m = data[0]
        chain = data[1:]
        for i in range(m - 1):
            graph[chain[i]].add(chain[i + 1])

    friend_counts = [len(graph[i]) for i in range(1, N + 1)]

    longest_chain = 0
    for i in range(1, N + 1):
        longest_chain = max(longest_chain, dfs(i, {i}, graph))

    print(f"#{tc}", " ".join(map(str, friend_counts)), longest_chain)
