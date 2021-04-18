import sys
sys.stdin = open("1242.txt", "r")
def Bbit_print(i):
    global output
    output = ""
    for j in range(3, -1, -1): # 앞에 비트가 많을텐데 앞에꺼 다 빼고 4개만 생각한다
        output += "1" if i & (1 << j) else "0"
    return output


for tc in range(1, int(input()) +1):
    pas = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9,
           '00000011110011':0, '00001111000011':1, '00001100001111':2, '00111111110011':3, '00110000001111':4, '00111100000011': 5, '00110011111111': 6, '00111111001111':7, '00111100111111':8, '00000011001111': 9}

    hexa = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15}

    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    ans = 0
    # print(arr)
    s = [] # 암호 있는 줄 뽑아오기. 근데 한줄에 여러개 있는거 어케 뽑아오지?
    for i in range(n):
        if arr[i].count('0') != len(arr[i]):
            s = arr[i]

            break
    # print(s)
    # 16진수를 10진수로 변환한 리스트
    h_lst = []
    for i in range(len(s)):
        if s[i] != '0':
            h_lst = s[i:i+15]
            break
    b = []
    for i in range(len(h_lst)):
        for k, v in hexa.items():
            if h_lst[i] == k:
                b.append(hexa[k])
    # print(b)
    binn = '' # 이제 그걸 이진수로 변환한것
    for i in b:
        binn += Bbit_print(i)

    # print(binn)
    new = []
    for i in range(len(binn) - 1, -1, -1):
        # 뒤에서 부터 탐색하면서 1 있는 곳부터 거꾸로 뽑아오기
        if binn[i] == '1':
            # print(i)
            for j in range(i, -1, -1):
                new.append(binn[j])
            break

    sp = []
    if len(new) < 112:
        for i in range(len(new) // 7):
            # 뒤에서 부터 뽑아줘서 거꾸로 뒤집어줘야한다
            sp.append(reversed(new[i * 7:i * 7 + 7]))
    if 112 <= len(new) < 280:
        for i in range(len(new) // 14):
            # 뒤에서 부터 뽑아줘서 거꾸로 뒤집어줘야한다
            sp.append(reversed(new[i * 14:i * 14 + 14]))
    else:
        for i in range(len(new) // 21):
            # 뒤에서 부터 뽑아줘서 거꾸로 뒤집어줘야한다
            sp.append(reversed(new[i * 21:i * 21 + 21]))

    p = []
    for i in range(len(sp) - 1, -1, -1):
        a = ''.join(sp[i])
        for k, v in pas.items():
            if a == k:
                p.append(v)

    result1 = 0
    result2 = 0
    for i in range(len(p) // 2):
        result1 += p[i * 2] * 3
        result2 += p[i * 2 + 1]
        ans = result1 + result2
    if ans % 10 == 0:
        result = sum(p)
        print('#{} {}'.format(tc, result))
    else:
        print('#{} {}'.format(tc, 0))


