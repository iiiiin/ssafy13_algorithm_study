# 프림
import heapq

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            dist = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 # 점들 간의 거리 계산
            cost = E * dist
            adj[i].append((cost, j)) # 인접 리스트에 저장
            adj[j].append((cost, i))


    visited = [0] * N
    pq = [(0, 0)]
    total_cost = 0 
    cnt = 0

    while pq:
        if cnt >= N: break # 모든 노드 다 돌았다면 break

        cost, node = heapq.heappop(pq)
        if visited[node]: continue

        visited[node] = 1 # 방문 체크
        total_cost += cost # 총 거리 계산
        cnt += 1

        for next_cost, next_node in adj[node]:
            if not visited[next_node]: # 방문하지 않은 경우만
                heapq.heappush(pq, (next_cost, next_node))

    print(f'#{tc} {round(total_cost)}')

# 크루스칼
def find_set(n):
    if boss[n] == n: return n
    boss[n] = find_set(boss[n])
    return boss[n]
 
def union_set(t1, t2):
    a = find_set(t1)
    b = find_set(t2)
    if a == b: return
    boss[b] = a
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())
    boss = [i for i in range(N)]
    points = []
    sum_v = 0
    for i in range(N):
        for j in range(i+1, N):
            L = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 # 거리 계산
            price = e * L # 비용 계산
            points.append((price, i, j))
    points.sort()
    
    for price, a, b in points:
        if find_set(a) == find_set(b): continue
        union_set(a, b)
        sum_v += price
 
    print(f'#{tc} {round(sum_v)}')