def solve(x):
    # 인덱스 범위 맞춰주기
    if x <= n:
        if tree[x] == 0: # 노드에 값이 없으면
            # 왼쪽
            left = solve(x*2)
            # 오른쪽
            right = solve(x*2 + 1)
            # 현재 노드에 왼쪽, 오른쪽 값 더해서 넣기
            tree[x] = left + right
            return tree[x]
    # 인덱스 넘어가면
    elif x > n:
        return 0
    if tree[x]:
        return tree[x]


for tc in range(1, int(input()) + 1):
    n, m, l = map(int, input().split())
    tree = [0] * (n + 1)
    for _ in range(m):
        node, number = map(int, input().split())
        # 일단 노드에 번호 넣기
        tree[node] = number
    # 노드번호 1번부터 시작이니까
    solve(1)
    # print(tree)
    print('#{} {}'.format(tc, tree[l]))