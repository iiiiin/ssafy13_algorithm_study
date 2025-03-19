from collections import deque

def bfs():
    q = deque()
    q.append((home_x, home_y)) # 집에서 시작

    while q:
        now_x, now_y = q.popleft()
        # 현재 위치에서 페스티벌 위치까지 1000 이하라면 행복하게 갈 수 있음
        if abs(now_x - festival_x) + abs(now_y - festival_y) <= 1000:
            return 'happy'

        for i in range(n):
            if visited[i]: continue # 방문했다면 건너뛰기
            x, y = store[i]
            # 편의점까지 갈 수 있다면
            if abs(now_x - x) + abs(now_y - y) <= 1000:
                q.append((x, y)) # 좌표 저장(예약걸기)
                visited[i] = 1 # 방문 표시
    return 'sad'

T = int(input())
for _ in range(T):
    n = int(input()) # 편의점 개수
    home_x, home_y = map(int, input().split()) # 집 좌표
    store = []
    for _ in range(n):
        x, y = map(int, input().split())
        store.append((x, y)) # 편의점 좌표
    festival_x, festival_y = map(int, input().split()) # 페스티벌 좌표
    visited = [0] * (n+1)
    print(bfs())