N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1) # 가치 저장할 리스트

for w, v in items: # weight, value
    for now_w in range(K, w-1, -1): # 뒤에서부터 거꾸로(중복 방지)
        dp[now_w] = max(dp[now_w], dp[now_w - w] + v) # 원래 저장되어있던 값과 (weight의 value + 남은 공간에 넣을 수 있는 가치)를 비교해서 최소값

print(dp[K])