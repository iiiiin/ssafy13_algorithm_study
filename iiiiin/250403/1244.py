# 1244
# [S/W 문제해결 응용] 2일차 - 최대 상금

'''
재귀로 입력받은 교환횟수만큼 완전탐색 수행
'''


def exchange(temp):
    global cnt, max_v
    if cnt == n:
        max_v = max(max_v, int(''.join(temp)))
        return

    rec = (''.join(temp), cnt)
    if rec in visited:
        return
    visited.add(rec)

    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            cnt += 1
            exchange(temp)
            num[i], num[j] = num[j], num[i]
            cnt -= 1


T = int(input())

for tc in range(1, T + 1):
    num, n = input().split()
    num = list(num)
    n = int(n)
    cnt = 0
    max_v = 0
    # dp(?) 메모이제이션
    visited = set()
    exchange(num)
    print(f'#{tc} {max_v}')
