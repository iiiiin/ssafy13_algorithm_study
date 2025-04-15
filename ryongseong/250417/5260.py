T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    queue = [(N, 0)]
    while queue:
        r, s = queue.pop()
        if r == 0:
            continue

        bound = r * (r+1) // 2 + s
        if bound >= K:
            if r + s == K:
                cnt += 1
            elif r + s < K:
                queue.append((r-1, r + s))
            queue.append((r-1, s))

    print(f'#{test_case} {cnt}')
