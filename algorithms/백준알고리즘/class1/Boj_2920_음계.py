numbers = list(map(int, input().split(' ')))
cnt1 = 0
cnt2 = 0
for i in range(len(numbers)-1):
    if numbers[i] < numbers[i+1]:
        cnt1 += 1
    elif numbers[i] > numbers[i + 1]:
        cnt2 += 1

if cnt1 == len(numbers)-1:
    print('ascending')
elif cnt2 == len(numbers)-1:
    print('descending')
else:
    print('mixed')
