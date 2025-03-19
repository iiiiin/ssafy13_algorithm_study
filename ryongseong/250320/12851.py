from collections import deque

N, K = map(int, input().split())

visited = [0] * 100001
cnt = 0
queue = deque([N])

min_time = float("inf")

while queue:
    x = queue.popleft()

    if x == K:
        if visited[x] < min_time:
            min_time = visited[x]
            cnt = 1
        elif visited[x] == min_time:
            cnt += 1
        continue

    for i in (x - 1, x + 1, x * 2):
        if 0 <= i < 100001:
            if not visited[i] or visited[i] == visited[x] + 1:
                visited[i] = visited[x] + 1
                queue.append(i)

print(min_time)
print(cnt)
