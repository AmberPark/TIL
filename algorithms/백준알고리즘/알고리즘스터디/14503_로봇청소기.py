def solve(r, c, d):
    global cnt
    visited.append((r, c))
    cnt += 1

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # a, b
        if 0<= nr < n and 0 <= nc < n and (nr, nc) not in visited and arr[nr][nc] == 0:
            solve(nr, nc, i)

        # c, d

        elif (nr, nc) in visited and arr[nr][nc] == 1:
            # 한칸 후진하고 돌아가기?
            i = (d + 2) % 4
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and arr[nr][nc] == 1:
                return
            else:
                solve(nr, nc, i)


n, m = map(int, input().split())
r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
visited = []
solve(r, c, d)
print(cnt)