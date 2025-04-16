def dfs(product, sum_v):
    global min_v

    if sum_v >= min_v: return # 이미 최소값보다 크다면 return

    if product == N: # 끝까지 탐색했으면
        min_v = min(min_v, sum_v) # 값 비교
        return

    for idx in range(N):
        if visited[idx] == 0:
            visited[idx] = 1
            dfs(product + 1, sum_v + arr[product][idx]) # 상품은 순서대로 선택
            visited[idx] = 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N # 공장 선택은 방문 배열로 체크하기
    min_v = float('inf')

    dfs(0, 0)

    print(f'#{t} {min_v}')