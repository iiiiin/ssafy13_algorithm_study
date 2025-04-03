def start(arr, N): # 0이 아닌 곳의 좌표 찾기
    for r in range(N):
        for c in range(N):
            if arr[r][c] != 0:
                return r, c
    return None, None

def row(start_r, start_c): # 가로 길이
    for i in range(1, N - start_r):
        if arr[start_r + i][start_c] == 0:
            return i
    return N - start_r

def col(start_r, start_c): # 세로 길이
    for j in range(1, N - start_c):
        if arr[start_r][start_c + j] == 0:
            return j
    return N - start_c

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    r_lst = []
    c_lst = []

    while True:
        start_r, start_c = start(arr, N)

        if start_r is None or start_c is None:
            break

        size_row = row(start_r, start_c)
        r_lst.append(size_row) # 가로 길이 저장

        size_col = col(start_r, start_c)
        c_lst.append(size_col) # 세로 길이 저장

        for i in range(size_row):
            for j in range(size_col):
                arr[start_r + i][start_c + j] = 0  # 해당 부분 제거

    result = list(zip(r_lst, c_lst))

    result = sorted(result, key=lambda x: (x[0] * x[1], x[0])) # 1.행과 열 곱한 값, 2.행 크기 작은 순서대로

    total_result = []

    for x, y in result:
        total_result.append(x)
        total_result.append(y)

    print(f'#{test_case} {len(result)}', *total_result)