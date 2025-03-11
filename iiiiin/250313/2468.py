# 2468. 안전 영역

'''
내리는 비의 양을 늘리면서 최댓값 갱신
내리는 비의 양이 i 일 때, DFS로 모든 지점에서 최대가 되는 값 찾기
i를 min ~ max 값 까지 순회하면서 최대값 업데이트
'''

import sys
input = sys.stdin.readline

def dfs(si,sj,threshold):
    # 방문 배열을 만들지 않고, 배열의 값을 직접 수정(다시 방문 못하게)

    if temp[si][sj] <= threshold or temp[si][sj] == 101:
        return 0
    # 시작점 방문 처리
    temp[si][sj] = 101
    # 스택 생성, 시작점 넣기
    stack = [(si,sj)]

    # 스택이 비어 있지 않을 동안 반복
    while stack:
        # 최근 이동 노드 확인
        r,c = stack.pop()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<N and 0<=nc<N and threshold<temp[nr][nc]<101:
                # 스택에 추가
                stack.append((nr,nc))
                temp[nr][nc] = 101

    # 배열의 값을 변경(탐색)했으면, 이것이 하나의 영역이므로 1개 반환
    return 1

N = int(input())
# 델타 배열
dr = [1,-1,0,0]
dc = [0,0,1,-1]
arr = [list(map(int, input().split())) for _ in range(N)]
# 내리는 비의 양에 따라 처리
max_v = max([max(x) for x in arr])
min_v = min([min(x) for x in arr])
result = 0
for rain in [0]+list(range(min_v, max_v+1)):
    temp = [x[:] for x in arr]
    cnt = 0
    for i in range(N):
        for j in range(N):
            cnt += dfs(i,j,rain)
    result = max(result, cnt)
print(result)


