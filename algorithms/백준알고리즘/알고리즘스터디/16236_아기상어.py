from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = deque()
t = 0
def eat(r, c):
    global t
    q = deque()
    q.append((r, c))
    # 자신보다 큰 물고기 칸은 못지나감, 작은 물고기만 먹을수 있음, 크기가 같은건 먹을수는 없지만 지나갈수는 있음.
    visited.append((r, c))
    while q:
        p = q.popleft()
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        for i in range(4):
            nr = p[0] + dr[i]
            nc = p[1] + dc[i]
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and 0 < arr[nr][nc] < arr[r][c]: # 작은 물고기
                visited.append((nr, nc))
                arr[nr][nc] = 0
                t += 1
                eat(nr, nc)
            elif 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and arr[nr][nc] == arr[r][c]:
                t += 1
                arr[r][c] += 1
                visited.append((nr, nc))
                eat(nr, nc)

        # elif 0 <= nr < n and 0 <= nc < n


for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            baby = [i, j]




eat(baby[0], baby[1])

print(t)