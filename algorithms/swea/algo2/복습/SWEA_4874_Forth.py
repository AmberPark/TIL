for tc in range(1, int(input())+1):
    lst = input().split()
    stk = []
    ans = ''
    for i in range(len(lst)):
        if lst[i].isdigit():
            stk.append(lst[i])
        elif lst[i] == '+':
            if len(stk) >1:
                a = int(stk.pop())
                b = int(stk.pop())
                stk.append(a+b)
            else:
                ans = 'error'
                break

        elif lst[i] == '-':
            if len(stk) >1:
                a = int(stk.pop())
                b = int(stk.pop())
                stk.append(b-a)
            else:
                ans = 'error'
                break
        elif lst[i] == '*':
            if len(stk) >1:
                a = int(stk.pop())
                b = int(stk.pop())
                stk.append(a*b)
            else:
                ans = 'error'
                break
        elif lst[i] == '/':
            if len(stk) >1:
                a = int(stk.pop())
                b = int(stk.pop())
                stk.append(b//a)
            else:
                ans = 'error'
                break

        elif lst[i] == '.':
            if len(stk) > 1:
                ans = 'error'
            else:
                ans = stk[-1]
    print('#{} {}'.format(tc, ans))

