# https://www.acmicpc.net/problem/2468
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 백준은 재귀 깊이가 10**3으로 되어있기에 10**6으로 설정 (안하면 RecursionError 발생)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 방향 배열 생성


def dfs(r, c, num):
    """
    r = 행 인덱스, c = 열 인덱스, num = 물의 높이
    구역의 수를 구하기에 물에 잠기지 않는 그룹을 합치기 위해 사용
    """
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        # 보드 안이며 물에 잠기지 않았다면
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if matrix[nr][nc] > num:  # 다음 위치가 물의 높이보다 높다면
                visited[nr][nc] = 1  # 하나로 묶음
                dfs(nr, nc, num)  # 다음 재귀 진행


N = int(input())
matrix = []
answer = 1
max_height = float("-inf")

for _ in range(N):
    arr = list(map(int, input().split()))
    matrix.append(arr)

    for c in arr:
        max_height = max(c, max_height)  # 최대 높이 설정

for i in range(1, max_height):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0

    for r in range(N):
        for c in range(N):
            # 물의 높이보다 높으며 그룹이 아니라면
            if matrix[r][c] > i and not visited[r][c]:
                cnt += 1  # 영역 수 증가
                visited[r][c] = 1  # 방문
                dfs(r, c, i)
    answer = max(answer, cnt)

print(answer)
