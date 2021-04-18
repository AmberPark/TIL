for tc in range(1, int(input())+1):
    string = input()
    stk = []
    ans = 1
    for i in range(len(string)):
        if string[i] == '{' or string[i] == '(':
            stk.append(string[i])

        elif string[i] == '}' or string[i] == ')':
           if stk:
               chk = stk.pop()
               if (chk == '(' and string[i] == '}') or (chk == '{' and string[i] == ')'):
                   ans = 0
           else:
               ans = 0

    if stk:
        ans = 0



    print('#{} {}'.format(tc, ans))





