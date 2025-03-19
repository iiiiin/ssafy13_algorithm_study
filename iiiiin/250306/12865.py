N, K = map(int, input().split())

# DP 테이블 초기화
dp = [[0] * (K+1) for _ in range(N+1)]

weights = []
values = []

for _ in range(N):
    # W: 물건의 무게, V: 물건의 가치
    W, V = map(int, input().split())
    weights.append(W)
    values.append(V)

for i in range(1,N+1):
    for w in range(1, K+1):
        # i번째 물건의 무게, 가치
        wi = weights[i-1]
        vi = values[i-1]

        # 현재 물건을 넣을 수 없다면
        if wi > w:
            dp[i][w] = dp[i-1][w]
        # 넣을 수 있다면
        else:
            # i번째를 안 넣을 때, 넣을 때
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-wi]+vi)

# N개의 물건을 고려하고, 허용 무게가 K일 때 최대 가치 합
print(dp[N][K])

