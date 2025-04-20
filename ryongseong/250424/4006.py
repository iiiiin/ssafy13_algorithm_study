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


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    parents = [i for i in range(N + 1)]
    M = int(input())
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: x[2], reverse=True)
    result = 0
    cnt = 0

    while edges:
        s, e, c = edges.pop()
        if cnt == N:
            break

        if find(s) != find(e):
            union(s, e)
            result += c
            cnt += 1

    print(f"#{test_case} {result}")
