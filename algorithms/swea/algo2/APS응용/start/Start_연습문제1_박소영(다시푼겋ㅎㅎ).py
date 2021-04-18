lst = list(input())
stk = []

for i in range(len(lst)//7):
    s = lst[i*7:i*7+7]
    stk.append(s)
# print(stk)
# for i in range(len(stk)):
#     result = 0
#     for j in range(len(stk[i]) - 1, -1, -1):
#         # print(i, j)
#         if stk[i][j] == '1':
#             a = 2 ** (len(stk[i])-j-1)
#             result += a
#         else:
#             a = 0
#
#     print(result, end=" ")
for i in range(10):
    result = 0
    for j in range(6, -1, -1):
        if stk[i][j] == '1':
            a = 2 ** (6-j)
            result += a
        else:
            a = 0

    print(result, end=" ")
# 0000000111100000011000000111100110000110000111100111100111111001100111