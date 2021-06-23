num = int(input())
for _ in range(num):
    cnt, s = input().split()
    result = ''
    for i in s:
        for j in range(int(cnt)):
            result += i
    print(result)