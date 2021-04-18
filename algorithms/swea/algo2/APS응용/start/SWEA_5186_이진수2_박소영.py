# 소수점 이진수 변환하는 함수
# 2로 곱한거에서 그 정수부분이 이진수의 첫째자리.
# 그다음 그 정수부분을 버리고 다시 2를 곱하고 같은 방식으로 쭉.
def solve(n):
    global ans
    if n != 0:
        if n * 2 >= 1:
            ans.append(1)
            solve(n * 2 -1)
        else:
            ans.append(0)
            solve(n * 2)
    else:
        return
    #     a = round(n * 2)
    #     ans.append(a)
    #
    #     solve(n * 2 - a)
    #
    # else:
    #     return
for tc in range(1, int(input()) + 1):
    b = float(input())
    ans = []
    solve(b)
    if len(ans) < 13:
        print('#{}'.format(tc), end=' ')
        for i in range(len(ans)):
            print(ans[i], end='')
        print()
    else:
        print('#{} overflow'.format(tc))
