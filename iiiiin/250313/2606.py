# 2606. 바이러스

'''
연결된 모든 컴퓨터를 감염시키고, 그 수를 확인
BFS
'''

from collections import deque

def dfs(start):
    global cnt
    # 노드 방문 처리
    visited = [0 for _ in range(V + 1)]
    # 큐 생성
    q = deque()
    # 시작점 큐 삽입, 방문처리
    q.append(start)
    visited[start] = 1
    # 큐가 빌 때까지 반복
    while q:
        v = q.popleft()
        for i in adj_list[v]:
            # 방문한 적이 없다면
            if not visited[i]:
                # 큐 삽입
                q.append(i)
                # 방문처리
                visited[i] = 1
                # 방문횟수 증가
                cnt += 1
    return cnt
# V: 노드 수
V = int(input())
# E: 간선 수
E = int(input())

# 노드(컴퓨터) 수가 적으므로 인접 리스트 사용
adj_list = [[] for _ in range(V+1)]
# 간선 수 만큼 쌍이므로, 입력 받기
for _ in range(E):
    s, e = map(int, input().split())
    # 무방향 그래프
    adj_list[s].append(e)
    adj_list[e].append(s)

# 컴퓨터 대수 변수 초기화, 시작점제외
cnt = 0
# dfs 함수 실행
print(dfs(1))