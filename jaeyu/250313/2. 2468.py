import sys
input = sys.stdin.readline 
sys.setrecursionlimit(1000000)  # 깊은 재귀 호출 허용, 호출의 최대 깊이

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# y, x 기준으로 높이 확인
def dfs(y, x, h):
    visited[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        # 다음 좌표가 배열 안의 범위에 있는지, 안전 영역인지, 아직 방문하지 않은 지역인지 확인
        if 0 <= ny < N and 0 <= nx < N and rain[ny][nx] > h and not visited[ny][nx]:
            dfs(ny, nx, h)

N = int(input())
rain = [list(map(int, input().split())) for _ in range(N)]
result = 0

for h in range(101):
	# 각 물 높이에 따라 안전 영역 초기화
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if rain[y][x] > h and not visited[y][x]:
                dfs(y, x, h)
                cnt += 1
    result = max(result, cnt)
print(result)