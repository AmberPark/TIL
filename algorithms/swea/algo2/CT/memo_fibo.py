def fibo_memo(n, memo_lst):
    if n < 2:
        return n
    if memo_lst[n] == 0:
        memo_lst[n] = fibo_memo(n-2, memo_lst) + fibo_memo(n-1, memo_lst)
    return memo_lst[n]

print(fibo_memo(10, [0]*11)) # 영부터 시작이니까 인덱스 하나 추가해야함
# => 55

# 계산되는 값이 n 가지니까 시간 복잡도 O(n)