lst = input()
bin = []
def Bbit_print(i):
    global output
    output = ""
    for j in range(3, -1, -1): # 앞에 비트가 많을텐데 앞에꺼 다 빼고 4개만 생각한다
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

# 여기서 쪼갠다!
stk = []
for i in range(len(b)//7):
    stk.append(b[i*7:i*7+7])
stk.append(b[len(b)//7 * 7:])  # 오 이렇게 // 하고 다시 곱하니까 나머지만 남는다!


# print(stk)
for i in range(len(stk)):
    result = 0
    for j in range(len(stk[i]) - 1, -1, -1):
        # print(i, j)
        if stk[i][j] == '1':
            a = 2 ** (len(stk[i])-j-1)
            result += a
        else:
            a = 0

    print(result, end=" ")


# 01D06079861D79F99F