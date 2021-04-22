def change(a:int):
    return a / 100

def solve(row, total):
    global maxx
    if total <= maxx:
        return

    if row == n:
        if total > maxx and total != 0: # 0 은 곱하면 0 이니까
            maxx = total
        return


    for i in range(n):
        if col_chk[i] == 0:
            col_chk[i] = 1
            solve(row + 1, total * arr[row][i]/100)
            col_chk[i] = 0


for tc in range(1, int(input()) +1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    col_chk = [0] * n
    maxx = 0
    solve(0, 1)

    print('#{} {:.6f}'.format(tc, maxx*100))