def heap_push(val):
    global idx
    idx += 1
    # 하나씩 트리에 넣으면서
    heap[idx] = val
    p = idx // 2
    ch = idx

    while p and heap[p] > heap[ch]:
        heap[p], heap[ch] = heap[ch], heap[p]
        ch = p
        p = ch // 2

for tc in range(1, int(input()) + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    # 트리
    heap = [0] * (n + 1)
    idx = 0

    for val in lst:
        heap_push(val)

    ans = 0
    node = n // 2
    while node:
        ans += heap[node]
        node = node // 2

    print('#{} {}'.format(tc, ans))