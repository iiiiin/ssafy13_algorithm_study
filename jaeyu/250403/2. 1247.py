def dfs(x1, y1, cnt, length):
    global min_length

    if length > min_length: return
    if cnt == N: # 좌표 다 돌았으면
        length += abs(home_x - x1) + abs(home_y - y1) # 마지막 좌표에서 집까지의 거리 계산
        min_length = min(min_length, length) # 길이 비교해서 값 갱신
        return

    for i in range(N):
        if used[i] == 1: continue # 방문했으면 건너뜀
        used[i] = 1 # 방문 표시
        x2, y2 = points[i]
        dist = abs(x1 - x2) + abs(y1 - y2) # 거리 계산
        dfs(x2, y2, cnt + 1, length + dist)
        used[i] = 0 # 방문 초기화

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    points = []
    min_length = float('inf')
    for i in range(0, len(arr), 2):
        points.append((arr[i], arr[i+1])) # 두 개씩 튜플로 저장
    company_x, company_y = points.pop(0)
    home_x, home_y = points.pop(0) 
    used = [0] * N
    dfs(company_x, company_y, 0, 0)

    print(f'#{tc} {min_length}')