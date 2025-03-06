# 시간을 최대한 줄이기

# 루트 사용, 입력 시간 단축
import math, sys

# N: 제곱수의 합으로 나타낼 수
N = int(sys.stdin.readline())

# DP테이블 초기화 0~N까지
dp = [i for i in range(N+1)]

# 반복문으로 dp테이블 값 갱신 -> 최솟 값(제곱수 항의 최소 개수) 찾기
# i: 제곱수의 합으로 나타낼 수, dp 테이블의 인덱스
for i in range(1, N+1):
    # j: 이전 값에 더해져 현재 i가 될 수 있는 값의 제곱근
    for j in range(1, int(math.sqrt(i)+1)):
        # 초기 dp[i]는 최악의 경우, 가장 큰 값
        # 현재 i가 될 수 있는 제곱근 항의 최소 개수보다
        # 이전 값에 j의 제곱을 더한 값이 더 작을 때
        # i > j*j 항상 성립
        # i- j*j > 0 이고, 인덱스, 항상 존재함
        # 모든 경우를 고려해서 최솟값을 갱신할 수 있음
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1

# N번째까지 실행되어 갱신된 결과 출력
print(dp[N])
