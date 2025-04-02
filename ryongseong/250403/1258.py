import heapq

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    dp = [[[0, 0] for _ in range(n + 2)] for _ in range(n + 2)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1]:
                left = dp[i][j - 1][0]
                up = dp[i - 1][j][1]
                dp[i][j][0] = left + 1
                dp[i][j][1] = up + 1

    answers = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] and (
                dp[i + 1][j][0] == 0
                and dp[i][j + 1][0] == 0
                and dp[i + 1][j][0] == 0
                and dp[i][j + 1][1] == 0
            ):
                heapq.heappush(
                    answers, (dp[i][j][0] * dp[i][j][1], dp[i][j][1], dp[i][j][0])
                )

    print(f"#{test_case} {len(answers)}", end="")
    for _ in range(len(answers)):
        tmp = heapq.heappop(answers)
        print(" {} {}".format(tmp[1], tmp[2]), end="")
    print()
