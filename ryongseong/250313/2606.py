# https://www.acmicpc.net/problem/2606

n = int(input())

varius = [False] * (n + 1)
pair_count = int(input())

pairs = [list(map(int, input().split())) for _ in range(pair_count)]


def dfs(node):
    varius[node] = True
    for a, b in pairs:
        if a == node and not varius[b]:
            dfs(b)
        elif b == node and not varius[a]:
            dfs(a)


dfs(1)
print(varius.count(True) - 1)


# def find(x):
#     if parents[x] != x:
#         parents[x] = find(parents[x])
#     return parents[x]


# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a != b:
#         parents[b] = a


# v = int(input())
# parents = [i for i in range(v + 1)]
# e = int(input())

# edges = [list(map(int, input().split())) for _ in range(e)]

# for edge in edges:
#     a, b = edge
#     union(a, b)

# print(sum(1 for i in range(1, v + 1) if find(i) == find(1)) - 1)
