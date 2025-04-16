T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    dp = [0] * (K + 1) # dp[i]는 합이 i가 되는 경우의 수
    dp[0] = 1 # 합이 0이 되는 경우는 공집합

    for i in range(1, N + 1):  # i를 더해서 합 만들기
        for j in range(K, i - 1, -1):  # 지금까지 만든 합에
            dp[j] += dp[j - i]

    print(f'#{tc} {dp[K]}')