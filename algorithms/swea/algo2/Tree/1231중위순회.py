import sys
sys.stdin = open("1231.txt", "r")
def solve(x):
    global stk
    if len(arr[x]) == 4: # 왼쪽 오른쪽 자식 둘다 연결되어있는거
        # 중위순회 => LVR
        # stk.append(int(arr[x][2])) # 왼쪽꺼 넣고
        solve(int(arr[x][2]))
        stk.append(arr[x][1]) # 루트 스택에 추가

        solve(int(arr[x][3])) # 오른쪽꺼

    elif len(arr[x]) == 3: # 왼쪽 하나만 연결되어 있는거
        solve(int(arr[x][2]))
        stk.append(arr[x][1])
    else: # 꽁다리들
        stk.append(arr[x][1])

    # return

for tc in range(1, 11):
    N = int(input())

    arr = [[0]] + [list(input().split()) for _ in range(N)] # 인덱스 맞춰주기
    stk = []
    solve(1)

    # print(stk)
    print('#{}'.format(tc), end=" ")
    for i in range(len(stk)):
        print(stk[i], end='')
    print()
