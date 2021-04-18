# def inorder(x):
#     if x <= n:
#         if len(arr[x]) == 4:
#             left = inorder(int(arr[x][2]))
#             right = inorder(int(arr[x][3]))
#             if arr[x][1] == '+':
#
#                 tree[int(arr[x][0])] = left + right
#                 return
#             elif arr[x][1] == '-':
#                 # left = inorder(int(arr[x][2]))
#                 # right = inorder(int(arr[x][3]))
#                 tree[int(arr[x][0])] = int(left) - int(right)
#                 return
#             elif arr[x][1] == '*':
#                 # left = inorder(int(arr[x][2]))
#                 # right = inorder(int(arr[x][3]))
#                 tree[int(arr[x][0])] = left * right
#                 return
#             elif arr[x][1] == '/':
#                 # left = inorder(int(arr[x][2]))
#                 # right = inorder(int(arr[x][3]))
#                 tree[int(arr[x][0])] = left // right
#                 return
#
#         else:
#             tree[int(arr[x][0])] = arr[x][1]
#             return tree[int(arr[x][0])]
#     else:
#         return tree
#
#
# for tc in range(1, 11):
#     n = int(input())
#     arr = [[0]] + [list(input().split()) for _ in range(n)]
#     tree = [0] * (n + 1)
#     inorder(1)
#     print(tree)
#     print('#{} {}'.format(tc, tree[1]))
def solve(n):
    if tree[n] == '-' or tree[n] =='+' or tree[n] =='*' or tree[n] =='/': # 뿌리노드가 연산자일때
        a = solve(ch[n][0])
        b = solve(ch[n][1])
        if tree[n] == '-':
            return a-b
        elif tree[n] == '+':
            return a + b
        elif tree[n] == '*':
            return a * b
        elif tree[n] == '/':
            return a//b
    else: # 아니면 그거 리턴
        return tree[n]

for tc in range(1, 11):
    N = int(input())
    arr = [[0]] + [list(input().split()) for _ in range(N)]
    tree = [0]
    ch = [[0,0] for _ in range(N+1)]
    # print(arr)
    for i in range(1, N+1):
        if len(arr[i]) == 4: # 왼쪽 오른족 노드 다 연결 돼있을 때
            tree.append(arr[i][1])
            ch[int(arr[i][0])][0] = int(arr[i][2]) # 왼쪽
            ch[int(arr[i][0])][1] = int(arr[i][3]) # 오른쪽
        else:
            tree.append(int(arr[i][1]))
    result = solve(1)
    print('#{} {}'.format(tc, result))