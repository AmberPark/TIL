def solve(r, c):
    q = []
    q.append((r, c))
    visited.append((r, c))
    while q:
        t = q.pop(0)
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        for i in range(4):
            nr = t[0] + dr[i]
            nc = t[1] + dc[i]
            if 0 <= nr < 16 and 0 <= nc < 16 and (nr, nc) not in visited and miro[nr][nc] != 1:
                q.append((nr, nc))
                visited.append((nr, nc))

for tc in range(1, 11):
    t_c = int(input())
    miro = [list(map(int, input())) for _ in range(16)]
    visited = []
    ans = 0
    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                start = (i, j)
            if miro[i][j] == 3:
                end = (i, j)

    solve(start[0], start[1])

    if (end[0], end[1]) in visited:
        ans = 1
    else:
        ans = 0
    print('#{} {}'.format(tc, ans))