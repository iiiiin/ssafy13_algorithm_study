import heapq


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    x_points = list(map(int, input().split()))
    y_points = list(map(int, input().split()))
    E = float(input())

    result = 0

    parents = [i for i in range(N)]
    edges = []

    for i in range(N):
        for j in range(i + 1, N):
            edges.append(
                ((E * ((abs(x_points[i] - x_points[j]) ** 2 + abs(y_points[i] - y_points[j]) ** 2) ** 0.5) ** 2, i, j)))
    edges.sort()

    for cost, s, e in edges:
        if parents.count(0) == N:
            break

        if find(s) != find(e):
            result += cost
            union(s, e)

    print(f"#{test_case} {round(result)}")
