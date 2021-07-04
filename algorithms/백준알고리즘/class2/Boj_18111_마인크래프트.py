n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
time = 0
for i in range(m-1):
    for j in range(n):
        if land[i][j] > land[i+1][j]:
            land[i+1][j] += (land[i][j]-land[i+1][j])
            time += land[i][j]-land[i+1][j]
        else:
            land[i+1][j] -= (land[i+1][j]-land[i][j])
            time += 2*(land[i+1][j]-land[i][j])
print(time, land[n][m])


