from collections import defaultdict


def dfs(node, depth):
    depths[node] = depth
    for child in tree[node]:
        if depths[child] == -1:
            parents[child] = node
            dfs(child, depth + 1)


def lca(a, b):
    while depths[a] > depths[b]:
        a = parents[a]
    while depths[b] > depths[a]:
        b = parents[b]

    while a != b:
        a = parents[a]
        b = parents[b]

    return a


def subtree_size(node):
    size = 1
    for child in tree[node]:
        size += subtree_size(child)
    return size


T = int(input())

for test_case in range(1, T + 1):
    V, E, a, b = map(int, input().split())
    edges = list(map(int, input().split()))

    tree = defaultdict(list)
    parents = [0] * (V + 1)
    depths = [-1] * (V + 1)

    for i in range(E):
        parent, child = edges[i * 2], edges[i * 2 + 1]
        tree[parent].append(child)
        parents[child] = parent

    parents[1] = 1
    dfs(1, 0)

    common_ancestor = lca(a, b)

    subtree_count = subtree_size(common_ancestor)

    print(f"#{test_case} {common_ancestor} {subtree_count}")
