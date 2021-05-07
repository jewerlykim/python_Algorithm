def solution(numbers, hand):
    answer = ''
    left = (3,0)
    right = (3,2)
    left_side = {1,4,7}
    right_side = {3,6,9}
    # key_pad = [[1,2,3],[4,5,6],[7,8,9]['*',0,'#']]

    for number in numbers:
        # print(left, right)
        if number in left_side:
            answer += 'L'
            left = (number//3, 0)
        elif number in right_side:
            answer += 'R'
            right = (number//3 - 1, 2)
        else:
            x, y =0, 0
            if number != 0:
                x, y = (number//3, 1)
            else:
                x, y = (3,1)
            count = abs(x - left[0]) + abs(y-left[1]) - abs(x - right[0]) - abs(y-right[1])
            # print(count)
            if count > 0:
                answer += 'R'
                right = (x, y)
            elif count < 0:
                answer += 'L'
                left = (x, y)
            else:
                if hand == 'right':
                    answer += 'R'
                    right = (x, y)
                else:
                    answer += 'L'
                    left = (x, y)
    # print(answer)


    return answer

solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")