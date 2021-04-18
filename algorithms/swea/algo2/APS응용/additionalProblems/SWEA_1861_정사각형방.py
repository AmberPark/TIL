def solve(r, c):
    global visited, cnt
    visited.append((r, c))
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]


for tc in range(1, int(input()) +1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            solve(i, j)