def solve(r, c):
    global q, total
    q.append((r, c))
    while q:
        t = q.pop(0)
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        for i in range(4):
            nr = t[0] + dr[i]
            nc = t[1] + dc[i]
            if 0 <= nr < n and 0 <= nc < n and total[nr][nc] == 0 and miro[nr][nc] != 1:
                q.append((nr, nc))
                total[nr][nc] = total[t[0]][t[1]] + 1

            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and miro[nr][nc] == 3:
                break

for tc in range(1, int(input()) + 1):
    n = int(input())
    miro = [list(map(int, input())) for _ in range(n)]
    visited = []
    q = []
    total = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 2:
                start = (i, j)
                solve(start[0], start[1])
            if miro[i][j] == 3:
                end = (i, j)

    # print(total)
    if total[end[0]][end[1]]:
        print('#{} {}'.format(tc, total[end[0]][end[1]] - 1))
    else:
        print('#{} {}'.format(tc, 0))
