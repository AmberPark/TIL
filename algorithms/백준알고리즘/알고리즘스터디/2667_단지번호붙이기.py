import sys
sys.stdin = open("2667.txt", "r")
N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
def dfs(r, c):
    global cnt
    visted[r][c] = 1 # 방문 체크 하고
    cnt += 1 # 개수 하나 증가시켜
    # 이제 주변 탐색
    # 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and visted[nr][nc] == 0 and arr[nr][nc] == 1:
            dfs(nr, nc)

visted = [[0] * N for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visted[i][j] == 0:
            cnt = 0
            dfs(i, j)
            result.append(cnt)

result.sort()
print(len(result))
for num in result:
    print(num)


