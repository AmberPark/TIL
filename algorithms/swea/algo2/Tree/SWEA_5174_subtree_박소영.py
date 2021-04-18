def solve(x):
    global cnt
    # 이제 더이상 새끼노드가 없으면 끝내기
    if x == 0:
        return
    # 카운트하고
    cnt += 1
    solve(left[x])
    solve(right[x])


for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0

    left = [0] * (E+2) # 노드번호는 1~ E+1 까지 존재하니까 인덱스 맞춰주기 위해 E+2akszma
    right = [0] * (E+2)

    for i in range(len(lst)//2):
        p = lst[i*2]
        ch = lst[i*2 + 1]

        if left[p] == 0: # 왼쪽에 자식이 없으면
            left[p] = ch
        else: # 왼쪽에 이미 자식이 있으면
            right[p] = ch # 자식은 오른쪽으로

    solve(N)
    print('#{} {}'.format(tc, cnt))




    