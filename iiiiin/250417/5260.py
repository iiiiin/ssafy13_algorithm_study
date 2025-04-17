def find_set(idx, temp):
    # memo는 (idx, temp)를 키로 결과(경우의 수)를 저장
    if (idx, temp) in memo:
        return memo[(idx, temp)]

    # 아직 고려하지 않은 원소들의 합
    r = pre_sum[idx]
    if temp > K:
        return 0
    if temp + r < K:
        return 0
    if temp + r == K:
        return 1
    if idx == N:
        return 1 if temp == K else 0

    # 원소를 포함하는 경우와 포함하지 않는 경우
    cnt = find_set(idx + 1, temp + arr[idx]) + find_set(idx + 1, temp)
    # 메모이제이션
    memo[(idx, temp)] = cnt
    # 재귀함수의 반환값
    return cnt


# 초기 입력 처리
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(range(1, N + 1))
    # 누적합 계산
    pre_sum = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        pre_sum[i] = pre_sum[i + 1] + arr[i]

    # 메모이제이션 딕셔너리
    memo = {}
    result = find_set(0, 0)
    print(f'#{tc} {result}')