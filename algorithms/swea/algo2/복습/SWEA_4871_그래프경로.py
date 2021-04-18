def dfs(start):
    visited.append(start)
    for i in range(v+1):
        if i not in visited and arr[start][i]:
            dfs(i)

for tc in range(1, int(input())+1):
    v, e = map(int,input().split())
    visited = []
    arr = [[0] * (v + 1) for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        arr[a][b] = 1
    s, g = map(int, input().split())

    dfs(s)
    if g in visited:
        print('#{} {}'.format(tc, 1))
    else:

        print('#{} {}'.format(tc, 0))


