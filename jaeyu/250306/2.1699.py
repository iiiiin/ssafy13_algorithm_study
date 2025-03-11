n = int(input())
dp = [k for k in range(n+1)] # 최대 갯수를 넣어놓은 것(제곱수 1로 구성된 경우)

for i in range(4, n+1):
    for j in range(1, i):
        if j * j > i: break
        if dp[i] > dp[i-j*j] + 1: # 최소 갯수를 넣어주는 것
            dp[i] = dp[i-j*j] + 1

print(dp[n])
