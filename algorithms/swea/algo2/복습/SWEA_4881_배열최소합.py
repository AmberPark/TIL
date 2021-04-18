def solve(row, total):
    global minn
    if row == N: # 끝까지 돌았을 때
        if total < minn:
            minn = total
            return
    if total >= minn:
        return
    for i in range(N):
        if col_chk[i] == 0:
            col_chk[i] = 1 # 방문했음 표시
            solve(row+1, total + arr[row][i])
            col_chk[i] = 0



for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col_chk = [0] * N
    minn = 987654321
    solve(0, 0)
    print('#{} {}'.format(tc, minn))