def dfs(cnt, current_r, current_c, dist):
    global min_dist
    if min_dist < dist:
        return
    if cnt == n:
        dist += abs(current_r - home[0]) + abs(current_c - home[1])
        min_dist = min(dist, min_dist)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            temp = (
                dist
                + abs(current_r - position_list[i][0])
                + abs(current_c - position_list[i][1])
            )
            dfs(cnt + 1, position_list[i][0], position_list[i][1], temp)
            visited[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))
    position_list = []
    visited = [0] * n
    min_dist = float("inf")

    for i in range(0, len(data), 2):
        position_list.append([data[i], data[i + 1]])
    company = position_list.pop(0)
    home = position_list.pop(0)

    dfs(0, company[0], company[1], 0)

    print(f"#{test_case} {min_dist}")
