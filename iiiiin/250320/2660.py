# 2660
# 회장뽑기

'''
회원번호 - 노드번호
연결관계 -> 인접리스트
최소 번호 -> 최소 방문 Lv.
각 노드에서 시작해서 최소 방문 Lv.을 찾고, 회장 후보인 노드 찾기
몇 사람을 통하면 모두가 서로 알 수 있다. => 연결되지 않은 노드는 없다.
'''

from collections import deque

def bfs(s):
    visited = [-1]*(N+1)
    q = deque()
    q.append(s)
    visited[s] = 0
    while q:
        now = q.popleft()
        for next in adj_list[now]:
            if visited[next] == -1:
                q.append(next)
                # 방문 리스트로 이동 경로의 깊이 저장
                visited[next] = visited[now] + 1

    # 완전히 탐색했을 때의 방문 Lv. 반환
    return max(visited)

# N: 회원수
N = int(input())

# 회원번호(노드번호) 인접 리스트, 번호 1부터 시작
adj_list = [[] for _ in range(N+1)]

# 마지막 줄 확인하고, 아닐 동안 반복
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    # 좌표를 입력받고 인접 리스트에 저장
    # 무방향 그래프
    adj_list[a].append(b)
    adj_list[b].append(a)

# 회장 후보 리스트 (후보노드, 점수) 형태 원소
candidates = []

for i in range(1,N+1):
    # 노드마다 함수를 실행하며 결과값 갱신
    candidates.append((i, bfs(i)))

min_score = min([x[1] for x in candidates])
entry = [x[0] for x in candidates if x[1] == min_score]

print(min_score, len(entry))
# 오름차순 출력
print(*sorted(entry))


