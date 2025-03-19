import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    visited = [0] * (num + 1)
    q = deque()
    q.append(n)
    visited[n] = 1

    while q:
        start = q.popleft()
        for next in tree[start]:
            if visited[next] == 1: continue # 방문했다면 건너뛰기
            visited[next] = 1 # 방문표시
            q.append(next) # 예약걸기
            check[n][next] = check[n][start] + 1 # 앞에서부터 타고 들어온 거리 + 1
            check[next][n] = check[n][next] # 양방향이므로 양쪽 표시

num = int(input())
tree = [[] for _ in range(num+1)]
cnt = 0
candidate = []
score = []

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1: break
    tree[a].append(b) # 양방향이니까 둘 다 추가
    tree[b].append(a)
check = [[0] * (num+1) for _ in range(num+1)] # 거리 표시할 배열

for i in range(1, num+1):
    bfs(i)

for row in check:
    score.append(max(row)) # 행 돌면서 최댓값이 해당 행의 점수

min_v = min(score[1:]) # 최소 점수 찾기
for j in range(num+1):
    if score[j] == min_v: # 최소 점수라면
        cnt += 1 # 후보 수 증가
        candidate.append(j) # 후보 리스트에 추가

print(min_v, cnt)
print(*candidate)