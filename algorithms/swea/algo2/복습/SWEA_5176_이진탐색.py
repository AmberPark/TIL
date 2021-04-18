def tree(x):
    global cnt
    if 0 < x <= n:

        # 왼
        tree(x * 2) # 현재노드에서 곱하기 2 한게 왼쪽노드인덱스
        # 현재노드
        cnt += 1
        node[x] = cnt
        # 오른쪽 노드
        tree(x * 2 + 1) # 현재노드에서 곱하기 2 더하기 1 한게 오른쪽 노드 인덱스
    else:
        return


for tc in range(1, int(input()) + 1):
    n = int(input())
    node = [0] * (n + 1)
    cnt = 0

    tree(1)
    # print(node)
    print('#{} {} {}'.format(tc, node[1], node[n//2]))