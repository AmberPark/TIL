def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1): # 앞에 비트가 많을텐데 앞에꺼 다 빼고 8개만 생각한다
        output += "1" if i & (1 << j) else "0"
    print(output)


for i in range(-5, 6):
    # print("%3d = " % i, end='') # %3d => 앞에 세칸 확보하고 출력하기
    print('{} ='.format(i), end=' ')
    Bbit_print(i)
