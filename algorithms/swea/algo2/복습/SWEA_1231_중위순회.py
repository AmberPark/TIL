def solve(x):
    if x <= n:
        if len(arr[x]) == 4:
            solve(int(arr[x][2])) # 왼쪽
            stk.append(arr[x][1])
            solve(int(arr[x][3])) # 오른쪽
        elif len(arr[x]) == 3:
            solve(int(arr[x][2]))
            stk.append(arr[x][1])
        else:
            stk.append(arr[x][1])

    else:
        return


for tc in range(1, 11):
    n = int(input())

    arr = [[0]] + [list(input().split()) for _ in range(n)]

    stk = []
    solve(1)

    print('#{}'.format(tc), end=" ")
    for i in range(len(stk)):
        print(stk[i], end="")
    print()


