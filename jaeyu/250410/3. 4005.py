def dfs(node, cnt):
    global max_v
    visited[node] = 1 # 현재 노드 방문 처리
    max_v = max(max_v, cnt) # 최대 경로 길이 갱신
    
    for next in alist[node]:
        if not visited[next]:
            dfs(next, cnt+1)
            
    visited[node] = 0 # 방문 초기화

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    alist = [[] for _ in range(N+1)] # 인접 리스트
    check = [0] * (N+1) # 비밀 말한 횟수 저장
    max_v = float('-inf') # 최대 

    for _ in range(K):
        info = list(map(int, input().split()))
        person = info[0] # 비밀 들은 사람의 수
        secret = info[1:] # 전달 순서
				
				# 순서대로 연결
        for i in range(person-1):
            num1, num2 = secret[i], secret[i+1]
            if num2 in alist[num1]: continue
            alist[num1].append(num2) # 친한 친구 저장
            check[num1] += 1

    for j in range(1, N+1):
        visited = [0] * (N + 1)
        dfs(j, 0)

    print(f'#{tc}', end= ' ')
    print(*check[1:], end = ' ')
    print(max_v+1)