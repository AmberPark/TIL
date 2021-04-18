def tree(n):
    global cnt, N
    if n <= N:
        # 왼쪽 -> 현재노드 -> 오른쪽
        tree(n * 2)  # 왼쪽노드
        # 이제 왼쪽에 없으면 찍고
        cnt += 1
        lst[n] = cnt
        tree(n*2 + 1)# 오른쪽 노드
for tc in range(1, int(input())+1):
    N = int(input())

    lst = [0] * (N+1)
    cnt = 0
    tree(1)

    print('#{} {} {}'.format(tc, lst[1], lst[N//2]))

# N은 6일때
# n <- 1
# tree(1)
# tree(2)
# tree(4)
# 곱하기 2 가 N 보다 작으니까
# lst[4] = 1
# tree(2)로 돌아가서
# lst[2] = 2
# tree(5)
# lst[5] = 3
# tree(1)로 돌아가서
# lst[1] = 4
# 아까 왼쪽 노드 봤으니까 이제 오른쪽으로
# tree(3)
# tree(6)
# lst[6] = 5
# 마찬가지로 곱하기 2가 N 보다 크니까
# tree(3)으로 돌아가서
# lst[3] = 6
