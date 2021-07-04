tc = int(input())
for _ in range(tc):
    h,w,n = map(int, input().split())
    hotel = [[0] * w for _ in range(h)]

    cnt = 0
    for i in range(w):
        for j in range(h):
            hotel[j][i] = 1
            cnt += 1
            if cnt == n:
                print((j+1)*100+ i+1)

