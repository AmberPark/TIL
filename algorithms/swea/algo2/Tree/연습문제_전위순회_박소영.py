import sys
sys.stdin = open("전위순회구현.txt", "r")
# 전위
def solve(x):
    global stk
    if len(arr[x]) == 3: # 왼쪽 오른쪽 둘다 연결돼있을때
        # 루트 넣고
        stk.append(arr[x][0])
        solve(arr[x][1]) # 왼쪽
        solve(arr[x][2]) # 오른쪽
    # 왼쪽만 연결돼 있을때
    elif len(arr[x]) == 2:
        stk.append(arr[x][0])
        solve(arr[x][1]) # 왼쪽
    # 꽁다리들
    else:
        stk.append(arr[x][0])

arr = [[0]]+[list(map(int, input().split())) for _ in range(13)]

stk = []
solve(1)
print(*stk)

