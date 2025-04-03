def dfs(cnt, number):
    global max_v

    if number in temp: return # 이미 있다면 return
    temp.append(''.join(num_list))

    if cnt == change: # 교환 가능 횟수 도달
        max_v = max(max_v, int(number)) # 값 비교, 갱신
        return

    N = len(number)
    for i in range(N-1): # i번째, j번째 문자 교환
        for j in range(i+1, N):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            dfs(cnt+1, ''.join(num_list))
            num_list[i], num_list[j] = num_list[j], num_list[i] # 다시 원래대로


T = int(input())
for tc in range(1, T+1):
    num, change = input().split()
    num_list = list(num)
    change = int(change)
    temp = [] # 가능한 숫자 저장 리스트
    max_v = 0
    dfs(0, ''.join(num_list)) # 숫자가 아닌 문자열로
    print(f'#{tc} {max_v}')