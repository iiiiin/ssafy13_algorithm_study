def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def calculate_points(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


N, M = map(int, input().split())
parents = [i for i in range(1000001)]
points = [None] + [list(map(int, input().split())) for _ in range(N)]
exist_list = [set(map(int, input().split())) for _ in range(M)]

for a, b in exist_list:
    union(a, b)

result = 0
edges = []

for i in range(1, N):
    for j in range(i + 1, N + 1):
        edges.append((calculate_points(points[i], points[j]), i, j))

edges.sort()

for edge in edges:
    dist, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += dist

print(f"{result:.2f}")
