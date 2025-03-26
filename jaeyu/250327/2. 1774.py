import sys
input = sys.stdin.readline

def find_set(n):
    if boss[n] == n: return n
    result = find_set(boss[n])
    boss[n] = result
    return result

def union_set(t1, t2):
    a = find_set(t1)  # 부모 찾기
    b = find_set(t2)  # 부모 찾기
    if a == b: return
    boss[b] = a  # b가 a 밑으로 들어감

N, M = map(int, input().split())
points = []
edges = []  # 거리, 인덱스 좌표 저장 리스트
boss = [i for i in range(N)]  # 부모 리스트
sum_v = 0
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
for _ in range(M):
    a, b = map(int, input().split())
    union_set(a-1, b-1)  # 이미 연결되어 있다면 합침

for i in range(N):  # 각 점을 연결했을 때의 거리 계산
    for j in range(i+1, N):
        dist = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
        edges.append((dist, i, j))
edges.sort() 

for dist, a, b in edges:
    if find_set(a) == find_set(b): continue  # 같은 집합이면 사이클 발생, 건너뜀
    union_set(a, b)  # 아니라면 합침
    sum_v += dist  # 거리 누적 계산

print("{:.2f}".format(sum_v))