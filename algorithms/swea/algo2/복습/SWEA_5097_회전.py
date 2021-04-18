for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    for _ in range(m):
        a = lst.pop(0)
        lst.append(a)

    print('#{} {}'.format(tc, lst[0]))

