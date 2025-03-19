for _ in range(int(input())):
    N = int(input())
    hour_1, minute_10, minute_1 = N // 60, (N % 60) // 10, N % 10
    result = [0] * 5

    if minute_1 > 5:
        minute_10 += 1
        minute_1 -= 10

    if minute_10 > 3:
        hour_1 += 1
        minute_10 -= 6

    if minute_10 < 0 and minute_1 == 5:
        minute_10 += 1
        minute_1 -= 10

    result[0] = hour_1
    if minute_10 >= 0:
        result[1] = abs(minute_10)
    else:
        result[2] = abs(minute_10)

    if minute_1 >= 0:
        result[3] = abs(minute_1)
    else:
        result[4] = abs(minute_1)

    print(*result)
