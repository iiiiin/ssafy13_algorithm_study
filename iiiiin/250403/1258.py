# 1258
# [S/W 문제해결 응용] 7일차 - 행렬찾기

'''
완전탐색
방문배열 필요
'''


def bruteforce(si, sj):
    # 시작값 설정
    x, y = 0, 0
    # 인덱스 범위 확인 후 0이 아닐 때까지 개수 세기
    while si+x < N and sj+y < N and arr[si + x][sj + y] != 0:
        # 각 열, 행 별로 조건
        while si+x < N and sj+y < N and arr[si + x][sj + y] != 0:
            # 방문 처리
            visited[si + x][sj + y] = 1
            # 다음 열로 이동
            y += 1
        res_y = y
        y = 0
        # 다음 행으로 이동
        x += 1
    return [x, res_y]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = []
    cnt = 0
    # 방문하지 않은 지점에 대해 영역탐색 함수(bruteforce) 사용
    for i in range(N):
        for j in range(N):
            # 0도 아니고, 방문도 하지 않았다면
            if arr[i][j] != 0 and visited[i][j] == 0:
                result.append(bruteforce(i, j))
                cnt += 1
    print(f'#{tc}', cnt, end=' ')
    # 동일한 크기라면, 행 오름차순
    result.sort(key=lambda x: (x[0]*x[1], x[0]))
    for i in range(len(result)):
        if i == len(result) - 1:
            print(*result[i])
        else:
            print(*result[i],end=' ')
