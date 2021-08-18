tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    idx_list = [0 for i in range(n)]
    idx_list[m] = 1

    cnt = 0

    while True:
        if lst[0] == max(lst):
            cnt += 1
            if idx_list[0] == 1:
                print(cnt)
                break

            else:
                del lst[0]
                del idx_list[0]

        else:
            lst.append(lst[0])
            del lst[0]
            idx_list.append(idx_list[0])
            del idx_list[0]









