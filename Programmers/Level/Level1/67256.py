def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    left_num = [1, 4, 7, '*']
    right_num = [3, 6, 9, '#']
    mid_num = [2, 5, 8, 0]
    distance = [0] * 2

    for number in numbers:
        if number in left_num:
            answer += 'L'
            left = number
        elif number in right_num:
            answer += 'R'
            right = number
        else:
            if left in left_num:
                if left == '*':
                    distance[0] = abs(mid_num.index(0) - mid_num.index(number)) + 1
                else:
                    distance[0] = abs(mid_num.index(left + 1) - mid_num.index(number)) + 1
            elif left in mid_num:
                distance[0] = abs(mid_num.index(left) - mid_num.index(number))
            if right in right_num:
                if right == '#':
                    distance[1] = abs(mid_num.index(0) - mid_num.index(number)) + 1
                else:
                    distance[1] = abs(mid_num.index(right - 1) - mid_num.index(number)) + 1
            elif right in mid_num:
                distance[1] = abs(mid_num.index(right) - mid_num.index(number))

            if distance[0] < distance[1]:
                answer += 'L'
                left = number
            elif distance[0] > distance[1]:
                answer += 'R'
                right = number
            else:
                if hand == "right":
                    answer += 'R'
                    right = number
                else:
                    answer += 'L'
                    left = number

    return answer