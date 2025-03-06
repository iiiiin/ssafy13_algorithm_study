# https://www.acmicpc.net/problem/2468
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(r, c, num):
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if matrix[nr][nc] > num:
                visited[nr][nc] = 1
                dfs(nr, nc, num)


N = int(input())
matrix = []
answer = 1
max_height = float("-inf")

for _ in range(N):
    arr = list(map(int, input().split()))
    matrix.append(arr)

    for c in arr:
        max_height = max(c, max_height)

for i in range(1, max_height):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0

    for r in range(N):
        for c in range(N):
            if matrix[r][c] > i and not visited[r][c]:
                cnt += 1
                visited[r][c] = 1
                dfs(r, c, i)
    answer = max(answer, cnt)

print(answer)
