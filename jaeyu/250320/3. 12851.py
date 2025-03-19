from collections import deque
N, K = map(int, input().split())
d = [-1, 1, 2]
cnt = 0 # 최단 거리로 도달하는 방법의 수
second = 0 # 최단 시간
visited = [0] * 100001

q = deque()
q.append(N)
while q:
    x = q.popleft()
    if x == K:
        second = visited[x]
        cnt += 1
        continue
    for i in d:
        if i == 2:
            next = x * i
        else:
            next = x + i
        # next가 범위 내에 있는지, 아직 방문하지 않았거나 최단 시간에 도달 할 수 있다면 진행
        if 0 <= next < 100001 and (visited[next] == 0 or visited[next] == visited[x] + 1):
            visited[next] = visited[x] + 1
            q.append(next)

print(second)
print(cnt)