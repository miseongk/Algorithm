def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1, c2, c3 = 0, 0, 0
    a = [0] * 3
    for ans in answers:
        if c1 == len(s1):
            c1 = 0
        if c2 == len(s2):
            c2 = 0
        if c3 == len(s3):
            c3 = 0

        if s1[c1] == ans:
            a[0] += 1
        if s2[c2] == ans:
            a[1] += 1
        if s3[c3] == ans:
            a[2] += 1

        c1 += 1
        c2 += 1
        c3 += 1

    max = 0
    idx = -1
    for i in range(3):
        if max < a[i]:
            max = a[i]
            idx = i
    answer.append(idx + 1)
    for i in range(3):
        if idx != i and max == a[i]:
            answer.append(i + 1)
    return sorted(answer)

# [참고]
# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []

#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1

#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)

#     return result
