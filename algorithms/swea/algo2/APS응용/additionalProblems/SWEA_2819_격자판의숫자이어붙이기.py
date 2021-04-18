# def solve(r, c):
#     global res
#     res.append(arr[r][c])
#     cnt = 0
#     if cnt == 6:
#         return res
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < 4 and 0 <= nc < 4:
#             cnt += 1
#             solve(nr, nc)
#
# for tc in range(1, int(input()) +1):
#     arr = [list(map(int ,input().split()) for _ in range(4))]
#
#     total = []
#     res = []
#     for i in range(4):
#         for j in range(4):
#             solve(i, j)
#     # 다 넣고 중복된거 지우기
#     total.append(res)
#     my_set = set(total)
#     my_total = list(my_set)
#     print(my_total)
def find(r, c, s):
    global t
    if len(s)==7:
        t.add(s)
        return
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            find(nr, nc, s+str(arr[nr][nc]))

for tc in range(1, int(input()) +1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    t = set()
    # print(arr)
    for i in range(4):
        for j in range(4):
            find(i, j, str(arr[i][j]))
    print('#{} {}'.format(tc, len(t)))