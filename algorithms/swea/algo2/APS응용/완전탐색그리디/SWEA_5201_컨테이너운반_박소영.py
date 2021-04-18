for tc in range(1, int(input()) +1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    new_w = sorted(w)[::-1]
    new_t = sorted(t)[::-1]
    ans = 0
    for i in range(min(n, m)): # 트럭 수가 짐 양보다 작을 수 있으니까. 안하면 인덱스에러
        if new_w[0] > new_t[0]: # 그 화물을 옮길 트럭이 없으면
            new_w.pop(0) # 그거 버리고
        else: # 있으면
            ans += new_w.pop(0) # 그 무게만큼 더하고
            new_t.pop(0) # 쓴 차도 빼주기

    print('#{} {}'.format(tc, ans))
