lst = input()
bin = []
def Bbit_print(i):
    global output
    output = ""
    for j in range(3, -1, -1):
        output += "1" if i & (1 << j) else "0"
    # print(output)

for i in range(len(lst)):
    if lst[i].isdigit():
        Bbit_print(int(lst[i]))
        bin.append(output)
    elif lst[i] == 'A':
        Bbit_print(10)
        bin.append(output)

    elif lst[i] == 'B':
        Bbit_print(11)
        bin.append(output)

    elif lst[i] == 'C':
        Bbit_print(12)
        bin.append(output)

    elif lst[i] == 'D':
        Bbit_print(13)
        bin.append(output)

    elif lst[i] == 'E':
        Bbit_print(14)
        bin.append(output)

    elif lst[i] == 'F':
        Bbit_print(15)
        bin.append(output)

# print(bin)
b = []
for i in range(len(bin)):
    for j in range(4):
        b.append(bin[i][j])
# print(b)

new_b = b[5:len(b)-5]
stk = []
# print(new_b)
for i in range(len(new_b)//6):
    s = new_b[i*6:i*6+6]
    stk.append(s)
# stk.append(new_b[len(new_b)//6 * 6:])
# print(stk)
ans = []
for i in range(len(stk)):
    p = ''.join(stk[i])
    # print(p)
    if p == '001101':
        ans.append(0)
    elif p == '010011':
        ans.append(1)
    elif p == '111011':
        ans.append(2)
    elif p == '110001':
        ans.append(3)
    elif p == '100011':
        ans.append(4)
    elif p == '110111':
        ans.append(5)
    elif p == '001011':
        ans.append(6)
    elif p == '111101':
        ans.append(7)
    elif p == '011001':
        ans.append(8)
    elif p == '101111':
        ans.append(9)


print(*ans)
# 0269FAC9A0
# 무식하게 반복했다,, 부끄럽