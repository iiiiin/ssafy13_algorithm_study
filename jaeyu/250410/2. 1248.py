def find_p(node): # 부모 노드 찾기
    new = [] # 부모 노드들 된 저장 리스트
    while node != 1:
        if node in left: # 왼쪽에 있다면
            for p_node in range(V+1):
                if left[p_node] == node: # 몇 번째에 있는지 찾으면 그 인덱스가 부모
                    new.append(p_node)
                    node = p_node # 갱신
                    break
        else: # 오른쪽에 있다면
            for p_node in range(V+1):
                if right[p_node] == node:
                    new.append(p_node)
                    node = p_node
                    break
    return new

def in_order(num): # 중위 순회, 서브 트리의 크기
    global cnt
    if num:
        in_order(left[num])
        cnt += 1
        in_order(right[num])

T = int(input())
for tc in range(1, T+1):
    V, E, a, b = map(int, input().split())
    info = list(map(int, input().split()))
    left = [0] * (V+1)
    right = [0] * (V+1)

    for i in range(E):
        parent = info[i * 2]
        child = info[i * 2 + 1]

        if left[parent] == 0: # 부모의 왼쪽이 비어 있다면 저장
            left[parent] = child
        else: # 비어 있지 않다면 오른쪽에 저장
            right[parent] = child

    list1 = find_p(a) # 조상 찾기
    list2 = find_p(b)

    for p in list1: # 같은 조상 있다면 반환
        if p in list2:
            result = p
            break

    cnt = 0
    in_order(result) # 중위 순회하여 노드 수 카운트

    print(f'#{tc} {result} {cnt}')