# 1247
# [S/W 문제해결 응용] 3일차 - 최적 경로

'''
재귀적으로 거리 계산해서 합구하기
가지치기 : min_v보다 크면 return(종료)
동시에 모든 지점으로 이동하는 경우 고려
'''

# cnt: 고객수, temp: 현재까지의 거리 합, start: 시작점
def dfs(cnt, temp, start):
    # 최솟값 전역변수
    global min_v
    # 가지치기 : 현재까지의 거리 합이 최솟값보다 크면 수행 종료
    if temp > min_v:
        return
    # 모든 고객을 방문했으면
    if cnt == N:
        # 마지막 고객에서 집까지의 거리 계산
        to_home = abs(start[0]-home[0])+abs(start[1]-home[1])
        # 이를 더한 최종 이동 거리와 최솟값 비교 후 갱신
        min_v = min(min_v, temp+to_home)
        return

    for i in range(N):
        # 방문하지 않은 모든 고객에 대해 각 경우의 수(DFS) 실행
        if not visited[i]:
            # 현재 지점에서 고객까지의 거리 계산
            to_spot = abs(start[0]-customer[i*2])+abs(start[1]-customer[i*2+1])
            # 방문 처리 후 재귀 수행
            visited[i] = 1
            dfs(cnt+1, temp+to_spot, (customer[i*2],customer[i*2+1]))
            visited[i] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    company = arr[:2]
    home = arr[2:4]
    customer = arr[4:]
    min_v = float('inf')
    visited = [0] * N
    dfs(0,0, company)
    print(f'#{tc} {min_v}')