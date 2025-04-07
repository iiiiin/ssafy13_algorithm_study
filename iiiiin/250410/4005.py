# 4005
# [Professional] 비밀

'''
비밀이동정보 => 인접리스트로 트리 연결 구조 표현
입력의 첫 숫자는 무시
트리를 구현 => DFS로 모든 트리를 이어보기
'''


def dfs(cur, cnt):
    global val
    # 재귀 함수 실행할 때마다 최댓값 갱신
    val = max(val, cnt)
    # 방문하지 않은 인접한 노드에 대해 재귀 함수 실행
    for nxt in adj_list[cur]:
        if not visited[nxt]:
            visited[nxt] = 1
            # 비밀 이동 거리 증가
            dfs(nxt, cnt + 1)
            visited[nxt] = 0


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # 인접 리스트
    adj_list = [set() for _ in range(N + 1)]
    for _ in range(K):
        temp = list(map(int, input().split()))
        # 시작 노드 무시하고 이후부터 수행
        for i in range(1, len(temp) - 1):
            # 연결된 노드 인접 리스트에 저장
            adj_list[temp[i]].add(temp[i + 1])
    # 최대 이동 거리
    val = 0
    # 인접 노드 개수 각각 반환
    result = [len(x) for x in adj_list[1:]]
    # 방문 리스트
    visited = [0] * (N + 1)
    for i in range(1, N + 1):
        # 방문 처리
        visited[i] = 1
        # 재귀함수 실행
        dfs(i, 1)
        # 방문 취소 처리
        visited[i] = 0
    print(f'#{tc}', *result, val)
