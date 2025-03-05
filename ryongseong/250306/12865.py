N, K = map(int, input().split())  # 물품의 수와 무게 입력 받아 할당

dp = [0] * (K + 1)  # dp 배열 생성

for _ in range(N):
    W, V = map(int, input().split())  # 무게와 가치를 입력받아 할당
    for i in range(
        K, W - 1, -1
    ):  # 버틸 수 있는 무게 부터 현재 입력받은 무게까지 역순으로 순회
        dp[i] = max(
            dp[i], dp[i - W] + V
        )  # 버틸 수 있는 무게 중에서 가치가 더 높은 것을 채택

print(dp[K])  # 최대로 버틸 수 있는 무게에서 가치의 최댓값 출력
