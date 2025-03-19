import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def color_blind(y, x, color):
    if arr[y][x] != color: return
    visited[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        # ny, nx가 범위 안에 있고 방문한 적이 없고 color가 같다면 탐색
        if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0 and arr[ny][nx] == color:
            color_blind(ny, nx, color)

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt_not, cnt = 0, 0

for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            color_blind(y, x, arr[y][x])
            cnt_not += 1

for y in range(N):
    for x in range(N):
	    # 적록색맹인 경우 R, G 구분이 안되기 때문에 하나의 색으로 통일
        if arr[y][x] == 'G':
            arr[y][x] = 'R'

visited = [[0]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            color_blind(y, x, arr[y][x])
            cnt += 1

print(cnt_not, cnt)