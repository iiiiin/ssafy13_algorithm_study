# 5209
# [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용

'''
0 ~ N-1까지의 인덱스에 대한 순열 구성
순열에 대한 모든 경우 DFS 수행
가지치기 수행
'''

def dfs(r, idx, temp):
    global min_v
    # 현재까지의 생산비용 합이 최솟값보다 크면 종료 (수행X)
    if temp > min_v:
        return
    # 마지막 행까지 인덱스를 선택했다면
    if r == N:
        # 최솟값 갱신 후 종료
        min_v = min(min_v, temp)
        return
    # 중복되지 않은 인덱스를 리스트에 추가하면서 생산비용 더하기
    for i in range(N):
        if i not in idx:
            # 다음 행에 대해 재귀함수 실행
            dfs(r+1, idx+[i], temp+arr[r][i])

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = float('inf')
    dfs(0, [], 0)
    print(f'#{tc} {min_v}')