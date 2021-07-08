while True:
    s = input()
    if int(s) == 0:
        break
    cnt = 0
    for i in range(len(s)//2):
        if s[i] == s[-i-1]:
            cnt += 1

    if cnt == len(s)//2:
        print('yes')
    else:
        print('no')



