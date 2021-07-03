n = 1
for _ in range(3):
    n *= int(input())

lst = [0] * 10

for i in range(10):
    for j in range(len(str(n))):
        if str(n)[j] == str(i):
            lst[i] += 1

for _ in range(10):
    print(lst[_])