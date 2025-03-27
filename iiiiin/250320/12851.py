# 12851
# 숨바꼭질 2

'''
BFS
다른 노드에서 동일한 노드로 이동할 수 있음
=> 최소 이동 보장(BFS), 동일한 깊이에서 동일한 노드에 도착 가능
횟수 세기(가장 빠른 시간으로 찾는 방법 수)
=> 단순 0, 1의 visited로는 사용 불가(visited는 1회만 확인)
'''

from collections import deque

def bfs(s):
    ways = [0] * (100000+1)
    q = deque()
    q.append(s)
    # t: 최소 소요 시간
    # cnt: 방법 수
    t, cnt = 0, 0
    while q:
        now = q.popleft()
        # 현재 노드까지 오는데 걸린 시간 저장
        val = ways[now]
        # 현재 노드가 동생 노드(위치)라면
        if now == K:
            # 도착하는 데 걸리는 시간(BFS로 구할 수 있는 최소 시간) 저장
            t = val
            # 방법 수 증가
            cnt += 1
            continue

        # 이동할 수 있는 경우 3가지
        temp = [now-1,now+1,now*2]
        for x in temp:
            # 이동 위치(노드)가 범위 안에 있는 지 확인
            if 0<= x <= 100000:
                # 방문한 적이 없거나, 이동 1회(1초 소요)로 이동가능하다면
                # 이동 1회란 -1로 도착하는 경우, +1로 도착하는 경우, *2로 도착하는 경우를 모두 고려
                if ways[x] == 0 or ways[x] == ways[now] + 1:
                    # 이동횟수를 갱신(추가)
                    ways[x] = ways[now] + 1
                    # 큐에 삽입
                    q.append(x)

    return t, cnt

N, K = map(int, input().split())
min_t, cases = bfs(N)
print(min_t, cases, sep='\n')