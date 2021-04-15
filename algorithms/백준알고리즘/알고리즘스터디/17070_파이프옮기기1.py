# 시간이 엄청 오래걸리는데.. 어케 줄이셨나요..?
# python3으로 해서 시간 초과가 나는데 pypy3으로 하면 시간 초과가 안난다는 것을 알게됏습니다. 그래도 오래걸리는 코드..

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
def move(r, c, di): # di : 방향. 0 => 우 , 1 => 우하 , 2=> 하
    global cnt
    # 끝에오면
    if r == n-1 and c == n-1:
        cnt += 1 # 끝 좌표에 온거니까 방법 하나 증가시키기
        return

    if di == 0: # 우방향으로 왔을때
        if r+1 < n and c+1 < n: # 인덱스 둘다 증가시킨게 범위 안이고
            if arr[r+1][c+1] == 0 and arr[r][c+1] == 0 and arr[r+1][c] == 0: # 대각선 방향으로 갈 수 있는 조건
                move(r+1, c+1, 1)
        if c+1 < n:
            if arr[r][c+1] == 0:
                move(r, c+1, 0)

    elif di == 1: # 대각선 방향으로 았을때
        if r+1 < n and c+1 < n: # 인덱스 둘다 증가시킨게 범위 안이고
            if arr[r+1][c+1] == 0 and arr[r][c+1] == 0 and arr[r+1][c] == 0: # 대각선 방향으로 갈 수 있는 조건
                move(r+1, c+1, 1)
        if c + 1 < n :
            if arr[r][c+1] == 0:
                move(r, c+1, 0)
        if r + 1 < n:
            if arr[r+1][c] == 0:
                move(r+1, c, 2)

    elif di == 2: # 우
        if r+1 < n and c+1 < n: # 인덱스 둘다 증가시킨게 범위 안이고
            if arr[r+1][c+1] == 0 and arr[r][c+1] == 0 and arr[r+1][c] == 0: # 대각선 방향으로 갈 수 있는 조건
                move(r+1, c+1, 1)
        if r+1 < n:
            if arr[r+1][c] == 0:
                move(r+1, c, 2)


move(0, 1, 0)
print(cnt)
# 펏 파이프 끝 좌표 (0, 1) 헷갈리지 말기


