num = int(input())

for _ in range(num):
    quiz = input()
    result = []
    cnt = 0
    for i in quiz:
        if i == 'O':
            cnt += 1
        else:
            cnt = 0
        result.append(cnt)
    print(sum(result))

