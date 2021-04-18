def game():
    count1 = [0] * 10
    count2 = [0] * 10
    for i in range(12):
        n = cards[i]
        if i % 2 == 0: # player1
            count1[n] += 1
            if count1[n] == 3: # triplet 검사
                return 1
            if run(count1): # run 검사
                return 1
        else:
            count2[n] += 1
            if count2[n] == 3:
                return 2
            if run(count2):
                return 2
    return 0

def run(count):
    for i in range(8):
        if count[i] >= 1 and count[i+1] >= 1 and count[i+2] >= 1:
            return 1

for tc in range(1, int(input()) +1):
    cards = list(map(int, input().split()))
    print('#{} {}'.format(tc, game()))