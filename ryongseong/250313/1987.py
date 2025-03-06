# https://www.acmicpc.net/problem/1987
import sys
from collections import deque

input = sys.stdin.readline

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(r, c, walk):
    global result
    result = max(result, walk)
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] not in visited:
            visited.add(matrix[nr][nc])
            dfs(nr, nc, walk + 1)
            visited.remove(matrix[nr][nc])


# def bfs():  # 시간초과 해결 불가
#     global result
#     queue = deque()
#     queue.append((0, 0, matrix[0][0]))

#     while queue:
#         r, c, alphabet = queue.popleft()
#         result = max(result, len(alphabet))
#         if result == 26: # 알파벳 최대수
#             return
#         for dr, dc in directions:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] not in alphabet:
#                 queue.append((nr, nc, alphabet + matrix[nr][nc]))


R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
result = 0
visited = set()
visited.add(matrix[0][0])

dfs(0, 0, 1)

# bfs()

print(result)
