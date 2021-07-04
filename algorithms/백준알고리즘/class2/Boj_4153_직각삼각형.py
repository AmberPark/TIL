while True:
    lst = sorted(list(map(int, input().split())))
    if sum(lst) == 0:
        break
    if lst[2]**2 == lst[0]**2 + lst[1]**2:
        print('right')
    else:
        print('wrong')
