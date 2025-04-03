def dfs(cnt, number):
    global max_v

    if number in temp: return
    temp.append(''.join(num_list))

    if cnt == change:
        max_v = max(max_v, int(number))
        return

    N = len(number)
    for i in range(N-1):
        for j in range(i+1, N):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            dfs(cnt+1, ''.join(num_list))
            num_list[i], num_list[j] = num_list[j], num_list[i]


T = int(input())
for tc in range(1, T+1):
    num, change = input().split()
    num_list = list(num)
    change = int(change)
    temp = []
    max_v = 0
    dfs(0, ''.join(num_list))
    print(f'#{tc} {max_v}')