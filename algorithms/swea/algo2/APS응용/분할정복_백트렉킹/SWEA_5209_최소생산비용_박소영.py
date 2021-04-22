def solve(row, total):
    global minn
    if row == n:
        if total <= minn:
            minn = total
    # 가지치기
    if total > minn:
        return

    for i in range(n):
        if col_chk[i] == 0: # 방문 안했으면
            col_chk[i] = 1
            solve(row + 1, total + arr[row][i])
            col_chk[i] = 0

for tc in range(1, int(input()) +1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    col_chk = [0] * n # 방문한 col인지 확인
    minn = 987654321
    solve(0, 0)
    print('#{} {}'.format(tc, minn))