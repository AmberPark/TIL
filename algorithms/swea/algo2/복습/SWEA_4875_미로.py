def solve(r, c):
    global ans
    visited.append((r, c))
    if miro[r][c] == 3:
        ans = 1
        return


    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited and miro[nr][nc] != 1:
            solve(nr, nc)


for tc in range(1, int(input()) + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = []
    ans = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start = (i, j)
                solve(start[0], start[1])

    print('#{} {}'.format(tc, ans))