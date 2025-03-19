# https://www.acmicpc.net/problem/10026
from collections import deque
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(r, c):
    queue.append((r, c))
    visited[r][c] = 1
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < N
                and 0 <= nc < N
                and matrix[nr][nc] == matrix[r][c]
                and not visited[nr][nc]
            ):
                visited[nr][nc] = 1
                queue.append((nr, nc))


def dfs(r, c, color):
    visited[r][c] = 1

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if matrix[nr][nc] == color:
                dfs(nr, nc, color)


N = int(input())
matrix = []

for _ in range(N):
    arr = []
    for c in list(input()):
        if c == "B":
            arr.append(1)
        elif c == "R":
            arr.append(2)
        else:
            arr.append(3)
    matrix.append(arr)

visited = [[0] * (N) for _ in range(N)]
queue = deque()
normal_cnt = 0
danger_cnt = 0

for color in range(1, 4):
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and matrix[r][c] == color:
                # bfs(r, c)
                dfs(r, c, color)
                normal_cnt += 1

for r in range(N):
    for c in range(N):
        if matrix[r][c] == 3:
            matrix[r][c] = 2

visited = [[0] * (N) for _ in range(N)]

for color in range(1, 3):
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and matrix[r][c] == color:
                dfs(r, c, color)
                # bfs(r, c)
                danger_cnt += 1

print(normal_cnt, danger_cnt)
