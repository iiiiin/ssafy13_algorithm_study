import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    result = [[int(1e9)] * N for _ in range(N)] # 최대 비용(10억)으로 저장
    y, x = start
    pq = [(MAP[y][x], start)]

    while pq:
        price, now = heapq.heappop(pq)
        y, x = now
        if result[y][x] < price: continue # 가려는 곳의 금액이 이미 크다면 확인할 필요 없음
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N: continue # 범위 벗어나는 경우 건너뜀
            next_price = MAP[ny][nx]
            price_sum = price + next_price
            if result[ny][nx] > price_sum: # 값 갱신
                result[ny][nx] = price_sum
                heapq.heappush(pq, (price_sum, (ny, nx))) # 다음 좌표 예약걸기

    return result

num = 1
while True:
    N = int(input())
    if N == 0: break
    MAP = [list(map(int, input().split())) for _ in range(N)]
    start = (0, 0) # 시작 좌표표
    result = dijkstra(start)
    print(f'Problem {num}: {result[N-1][N-1]}')
    num += 1