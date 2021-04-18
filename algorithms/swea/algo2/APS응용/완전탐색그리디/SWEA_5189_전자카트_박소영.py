def perm(idx):
    global res_lst

    if idx == len(lst):
        res_lst.append(lst[:])

    else:
        for i in range(idx, len(lst)):
            # 순서 바꾸고
            lst[idx], lst[i] = lst[i], lst[idx]
            perm(idx + 1)
            # 원상복귀
            lst[idx], lst[i] = lst[i], lst[idx]

for tc in range(1, int(input()) +1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    lst = []
    for i in range(2, n+1):
        lst.append(i) # 순열 돌릴 리스트 만들기
    res_lst = []
    total = []
    perm(0)
    # print(res_lst)
    for i in range(len(res_lst)):
        summ = 0
        for j in range(len(res_lst[i])-1):
            summ += arr[res_lst[i][j]-1][res_lst[i][j+1]-1]
        total.append(arr[0][res_lst[i][0]-1] + summ + arr[res_lst[i][-1]-1][0])
    # print(total)
    final = min(total)

    print('#{} {}'.format(tc, final))