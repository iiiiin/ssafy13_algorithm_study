# 9205
# 맥주 마시면서 걸어가기

'''
각 편의점과 집, 페스티벌 좌표를 모두 노드로 간주
집 -> 각 편의점 -> 페스티벌 로 가능 모든 경로 탐색
BFS 사용
조건: 이동할 수 있으면 이동(큐 삽입, 방문처리)
'''

from collections import deque

def bfs(si, sj):
    visited = [0] * n
    q = deque()
    q.append((si, sj))
    while q:
        r, c = q.popleft()
        # 현재위치에서 페스티벌로 이동가능한지 확인 (맨해튼 거리 계산)
        if abs(fr - r) + abs(fc - c) <= 1000:
            return 'happy'
        # 아니라면 각 편의점 좌표를 확인
        # 방문한 적이 없고, 이동가능하다면 (맨해튼 거리 계산)
        # 동일한 편의점에 다시 방문하더라도 이동할 수 있는 노드(편의점,페스티벌)는 동일
        # 따라서 1번만 방문(방문처리)
        for idx, x in enumerate(convenience):
            if abs(r-x[0]) + abs(c-x[1]) <= 1000 and not visited[idx]:
                q.append((x[0], x[1]))
                visited[idx] = 1
    # 이동가능한 모든 노드를 탐색했음에도 도착점(페스티벌)에 도달하지 못했다면
    return 'sad'


t = int(input())

for _ in range(t):
    n = int(input())
    # 집 좌표
    hr, hc = map(int, input().split())
    # 편의점 좌표 리스트
    convenience = [list(map(int, input().split())) for _ in range(n)]
    # 페스티벌 좌표
    fr, fc = map(int, input().split())
    # BFS 함수 실행
    result = bfs(hr,hc)
    print(result)

# DFS
# def dfs(r, c):
#     global result
#     if result == 'happy':
#         return
#     if abs(fr-r)+abs(fc-c) <= 1000:
#         result = 'happy'
#         return
#     for idx, x in enumerate(convenience):
#         if not visited[idx] and abs(x[0]-r) + abs(x[1]-c) <= 1000:
#             visited[idx] = 1
#             dfs(x[0], x[1])
#             # visited[idx] = 0
#             # 백트래킹 필요없음
#
# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     hr, hc = map(int, input().split())
#     convenience = [list(map(int, input().split())) for _ in range(n)]
#     fr, fc = map(int, input().split())
#     visited = [0] * n
#     result = 'sad'
#     dfs(hr,hc)
#     print(result)
