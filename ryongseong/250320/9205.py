import sys
from collections import deque

input = sys.stdin.readline


def cal_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) <= 1000


def bfs():
    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()
        if cal_manhattan((x, y), (end_x, end_y)):
            print("happy")
            return
        for i in range(n):
            if visited[i]:
                continue
            r, c = stores[i]
            if cal_manhattan((x, y), (r, c)):
                visited[i] = 1
                queue.append((r, c))

    print("sad")
    return


for _ in range(int(input())):
    n = int(input())
    start_x, start_y = map(int, input().split())
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    end_x, end_y = map(int, input().split())
    visited = [0] * (n + 1)
    bfs()
