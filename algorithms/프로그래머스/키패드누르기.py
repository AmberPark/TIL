def solution(numbers, hand):
    answer = ''
    last_L = 10
    last_R = 12

    left = [1, 4, 7]
    right = [3, 6, 9]
    mid = [2, 5, 8, 0]
    for num in numbers:
        if num in left:
            answer += 'L'
            last_L = num

        elif num in right:
            answer += 'R'
            last_R = num

        elif num in mid:
            if num == 0:
                num = 11

            absL = abs(num - last_L)
            absR = abs(num - last_R)

            # if (abs(num - last_L) == 2 and abs(num - last_R) == 4) or (abs(num - last_L) == 4 and abs(num - last_R) == 2) or (abs(num - last_L) == 5 and abs(num - last_R) == 7:

            if last_R in right and last_L in left and abs(absL - absR) == 2:
                if hand == "left":
                    answer += 'L'
                    last_L = num
                else:
                    answer += 'R'
                    last_R = num

            elif abs(absL - absR) == 2 and last_L in left or last_R in mid:
                if hand == "left":
                    answer += 'L'
                    last_L = num
                else:
                    answer += 'R'
                    last_R = num
            elif last_L == num - 3 and last_R == num - 2:
                answer += 'L'
                last_L = num

            elif abs(num - last_L) < abs(num - last_R):
                answer += 'L'
                last_L = num
            elif abs(num - last_L) > abs(num - last_R):
                answer += 'R'
                last_R = num

            else:
                if hand == "left":
                    answer += 'L'
                    last_L = num
                else:
                    answer += 'R'
                    last_R = num

    return answer


