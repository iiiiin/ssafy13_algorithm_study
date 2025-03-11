# 10026. 적록색약

'''
우선 델타 탐색, DFS
적록색약이 아닌 사람이 보는 구역 수
그리고, 적록색약인 사람 (R or G)이 보는 구역 수 구하기
'''

import sys
input = sys.stdin.readline

# dfs 함수
def dfs(si, sj):
    # 시작점이 방문했던 곳이라면
    if picture[si][sj] == 'X':
        return 0
    # 스택 생성
    stack = [(si,sj)]
    # 현재값 저장
    temp = picture[si][sj]
    # 방문 처리
    picture[si][sj] = 'X'
    # 스택이 비어있지 않을 동안 반복
    while stack:
        # 스택에서 최상단 하나 꺼내기
        r, c = stack.pop()
        # 델타 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 인덱스 범위 안에 있고, 방문한 적 없다면
            if 0<=nr<N and 0<=nc<N and picture[nr][nc] == temp:
                # 스택에 넣기
                stack.append((nr, nc))
                # 방문 처리
                picture[nr][nc] = 'X'
    # 현재까지의 묶음 1개
    return 1

def dfs_rg(si, sj):
    # 시작점이 방문했던 곳이라면
    if picture_rg[si][sj] == 'X':
        return 0
    # 스택 생성
    stack = [(si,sj)]
    # 현재값 저장
    temp = picture_rg[si][sj]
    # 방문 처리
    picture_rg[si][sj] = 'X'
    # 스택이 비어있지 않을 동안 반복
    while stack:
        # 스택에서 최상단 하나 꺼내기
        r, c = stack.pop()
        # 델타 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 인덱스 범위 안에 있고, 방문한 적 없다면
            if 0<=nr<N and 0<=nc<N:
                if temp in ['R' ,'G'] and picture_rg[nr][nc] in ['R','G']:
                    # 스택에 넣기
                    stack.append((nr, nc))
                    # 방문 처리
                    picture_rg[nr][nc] = 'X'
                elif picture_rg[nr][nc] == temp:
                    # 스택에 넣기
                    stack.append((nr, nc))
                    # 방문 처리
                    picture_rg[nr][nc] = 'X'
    # 현재까지의 묶음 1개
    return 1

N = int(input())
# 델타 배열
dr = [1,-1,0,0]
dc = [0,0,1,-1]
picture = [list(input()) for _ in range(N)]
picture_rg = [x[:] for x in picture]
# 적록색약 아닌 사람이 보는 구역 수, 적록색약인 사람이 보는 구역 수 계산
area = area_rg = 0
for i in range(N):
    for j in range(N):
        area += dfs(i,j)
        area_rg += dfs_rg(i,j)

print(area, area_rg)




