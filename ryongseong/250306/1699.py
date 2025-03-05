# https://www.acmicpc.net/problem/1699

N = int(input())  # 자연수 N 입력

dp = [0] * (N + 1)  # N까지의 dp 배열 생성

for i in range(1, N + 1):  # 1 ~ N까지 순회
    dp[i] = i  # 처음에는 1 ** 2를 이용하여 총 i개의 항을 사용하므로 i를 할당
    for j in range(1, i):  # i 값 이전에 가능한 제곱수를 찾는다
        if (j**2) > i:  # 만약 j ** 2가 i값 보다 크다면 만들 수 없으므로
            break  # j를 순회하는 반복문을 종료한다.
        dp[i] = min(dp[i], dp[i - j**2] + 1)  # dp[i] 자리에 이제 비교를 하여 값을 갱신
        # 여기서 dp[i - j ** 2] + 1을 하는 이유는 dp[i - j ** 2] 에서 j ** 2 항을 더 하면 되기에 1을 추가한다.

print(dp[N])  # 원하는 값 출력
