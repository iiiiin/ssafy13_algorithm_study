import sys
from collections import deque

input = sys.stdin.readline


def bfs(g: list, s: int):
    cnt = 0
    q = deque([(s, cnt)])
    n = len(g)
    vst = {node: 0 for node in range(1, n + 1)}
    vst[s] = 1

    while q:
        x, d = q.popleft()
        for n in g[x]:
            if vst[n]:
                continue
            q.append((n, d + 1))
            if cnt < d + 1:
                cnt = d + 1
            vst[n] = 1
    return cnt


n = int(input())
g = {node: [] for node in range(1, n + 1)}
while True:
    u, v = map(int, input().split())
    if u == v == -1:
        break
    g[u].append(v)
    g[v].append(u)

min_val = float("inf")
result = []
for i in range(1, n + 1):
    tmp = bfs(g, i)
    if tmp < min_val:
        min_val = tmp
        result = [i]
    elif tmp == min_val:
        result.append(i)

print(min_val, len(result))
print(*sorted(result))
