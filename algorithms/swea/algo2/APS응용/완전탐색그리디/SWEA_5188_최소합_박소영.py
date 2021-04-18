def solve(r, c, total):
    global minn

    if r == n-1 and c == n-1:
        if total < minn:
            minn = total
            return
    if total >= minn:
        return
    # 오른쪽, 아래
    dr = [0, 1]
    dc = [1, 0]
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
            visited.append((nr, nc))
            solve(nr, nc, total + arr[nr][nc])
            visited.remove((nr, nc))



for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int ,input().split())) for _ in range(n)]
    minn = 987654321
    visited = []
    solve(0, 0, arr[0][0])
    print('#{} {}'.format(tc, minn))