import heapq

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dijkstra(start):
    # 최소 비용 저장할 2차원 배열
    temp = [[float('inf')] * N for _ in range(N)]
    temp[0][0] = arr[0][0]
    q = [(0, start)] 

    while q:
        price, point = heapq.heappop(q)
        y, x = point

        # 이미 더 작은 비용으로 방문된 적이 있다면 스킵
        if temp[y][x] < price: continue

        # 4방향 탐색
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            # 범위 내, 더 적은 비용으로 갈 수 있다면 갱신신
            if 0 <= ny < N and 0 <= nx < N:
                next_price = arr[ny][nx]
                sum_v = price + next_price 
                if temp[ny][nx] > sum_v:
                    temp[ny][nx] = sum_v
                    heapq.heappush(q, (sum_v, (ny, nx)))
    
    # 도착 지점의 최소 비용 반환
    return temp[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start = (0, 0)
    result = dijkstra(start)
    print(f'#{tc} {result}')