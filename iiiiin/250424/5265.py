# 5265
# [파이썬 S/W 문제해결 최적화] 4일차 - 전기카트2

'''
순열 구하기
순열을 모두 구하고 계산하지 말고
순열을 구하면서 인자로 계산값을 넘겨줌
최소 소비량 찾기
=> DFS
=> 가지치기 : 현재 최솟값보다 크다면 함수 종료
'''


def dfs(si, cnt, v):
    global min_v

    # 현재 값이 최솟값보다 크다면 종료
    if v >= min_v:
        return

    # 모든 순열 완성하면
    if cnt == N:
        # 처음으로 돌아가는 방향추가
        v += arr[si-1][0]
        # 최솟값 갱신
        min_v = min(min_v, v)
        return

    # 순열 만들기
    for i in range(2,N+1):
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1, v+arr[si-1][i-1])
            visited[i] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = float('inf')
    visited = [0] * (N+1)
    # 1부터 시작
    dfs(1,1,0)
    print(f'#{tc} {min_v}')