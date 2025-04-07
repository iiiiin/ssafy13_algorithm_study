# 1248
# [S/W 문제해결 응용] 3일차 - 공통조상

'''
DFS(재귀)
노드 A에 노드 B의 부모를 처음부터 끝까지 찾고
노드 A의 모든 부모 경우로 수행
'''


def recur(r_a, r_b):
    # r_a의 부모와 같다면 부모 반환
    if parents[r_a] == find_par(r_a, r_b):
        return parents[r_a]
    # r_a의 부모에 대해 재귀 함수 실행
    return recur(parents[r_a], r_b)


def find_par(a, b):
    # 부모 노드가 같으면 종료
    if parents[a] == parents[b]:
        return parents[a]
    # 부모 노드가 0이면, 1(루트 노드)
    if parents[b] == 0:
        return 1
    # b의 부모 노드에 대해 재귀 함수 실행
    return find_par(a, parents[b])


def find_chd(x):
    global cnt
    # 모든 노드에 대해 자식 노드 찾기
    for j in range(V + 1):
        if parents[j] == x:
            # 개수 세기
            cnt += 1
            # 재귀 함수 실행
            find_chd(j)


T = int(input())

for tc in range(1, T + 1):
    V, E, A, B = map(int, input().split())
    linked = list(map(int, input().split()))
    parents = [0] * (V + 1)
    for i in range(E):
        # 연결 관계 기록
        parents[linked[i * 2 + 1]] = linked[i * 2]
    cnt = 0
    result = recur(A, B)
    # 그래프 연결된 노드로 계속 이동하면서 개수 세기
    find_chd(result)
    print(f'#{tc} {result} {cnt+1}')
