# 1251
# [S/W 문제해결 응용] 4일차 - 하나로

'''
각 섬을 모두 연결 => 트리?
환경부담금 = E * L^2 (0<=E<=1)
각 터널(간선)의 길이(가중치)가 최소인 트리 만들기
MST를 만들면서 min_weight로 환경부담금 계산 후 갱신
그리고 최종 환경부담금 반환
일단 Prim?
시작점 상관없고, 모든 노드가 연결된 MST 만들기
'''

from heapq import heappush, heappop

def prim(start):
    # 방문 처리용 리스트
    MST = [0] * N
    # 최소 가중치로 계산한 최소 거리(제곱)의 합
    # 그런데? 거리는 ((x2-x1)**2 + (y2-y1)**2))**0.5이므로
    # 제곱은 (x2-x1)**2 + (y2-y1)**2)
    min_fee = 0
    # 우선순위 큐 생성
    pq = [(0, start)]
    while pq:
        w, idx = heappop(pq)
        # 이미 방문했다면 continue
        if MST[idx]:
            continue
        # 방문 처리
        MST[idx] = 1
        # 누적합 추가
        min_fee += w

        # 모든 노드에 대해 탐색
        for next_idx in range(N):
            # 이미 방문했으면 pass
            if MST[next_idx]:
                continue
            # 현재 노드에서 다음 노드까지의 거리 구하기
            next_w = (x[next_idx]-x[idx])**2 + (y[next_idx]-y[idx])**2
            # 방문하지 않은 모든 노드를 우선순위 큐 삽입
            heappush(pq, (next_w, next_idx))

    return min_fee

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    result = E*prim(0)
    print(f'#{tc} {round(result)}')