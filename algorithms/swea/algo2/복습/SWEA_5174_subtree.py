def solve(n):
    global cnt
    if n:
        cnt += 1
        solve(left[n])
        solve(right[n])
    else:
        return

for tc in range(1, int(input()) + 1):
    e, n = map(int, input().split())
    nodes = list(map(int, input().split()))
    cnt = 0
    left = [0] * (e+2)
    right = [0] * (e+2)

    for i in range(len(nodes)//2):
        p = nodes[i*2]
        ch = nodes[i*2 + 1]

        if left[p] == 0:
            left[p] = ch
        else:
            right[p] = ch
    solve(n)

    print('#{} {}'.format(tc, cnt))