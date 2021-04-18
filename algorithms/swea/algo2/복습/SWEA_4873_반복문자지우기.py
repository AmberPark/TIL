def solve(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            string.pop(i)
            string.pop(i)
            solve(string)



for tc in range(1, int(input()) + 1):
    string = input()
    stk = []
    for i in range(len(string)):
        stk.append(string[i])
        solve(stk)


    print('#{} {}'.format(tc, len(stk)))