def dfs(n):
    global cnt
    visited[n] = 1
    for i in computer[n]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

N = int(input()) # 총 컴퓨터의 수
n = int(input()) # 실제 연결된 컴퓨터 수
computer = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

for _ in range(n):
    a, b = map(int, input().split())
    computer[a].append(b) # 양방향 연결 표현
    computer[b].append(a)
dfs(1)
print(cnt)