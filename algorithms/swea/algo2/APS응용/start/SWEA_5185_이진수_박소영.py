def Bbit_print(i):
    global output
    output = ""
    for j in range(3, -1, -1): # 앞에 비트가 많을텐데 앞에꺼 다 빼고 4개만 생각한다
        output += "1" if i & (1 << j) else "0"
hexa = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for tc in range(1, int(input()) + 1):
    n, h = input().split()

    bin = []
    for i in range(int(n)):
        for k, v in hexa.items():
            if h[i] == k:
                Bbit_print(hexa[k])
                bin.append(output)
    # print(bin)
    result = ''
    for i in range(len(bin)):
        result += bin[i]
    print('#{} {}'.format(tc, result))


