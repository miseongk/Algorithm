n = int(input())
input_list = [list(map(int, input().split())) for _ in range(n)]
data = sorted(input_list, key=lambda x: (x[0], x[1]))

result = 1
start = data[0][0]
end = data[0][1]
for i in range(1, len(data)):
    if start == data[i][0]:
        if start == end:
            end = data[i][1]
            result += 1
        elif end > data[i][1]:
            end = data[i][1]
    elif end <= data[i][0]:
        start = data[i][0]
        end = data[i][1]
        result += 1
    elif end > data[i][0]:
        if end > data[i][1]:
            start = data[i][0]
            end = data[i][1]
        else:
            continue

print(result)

# Sample Answer

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# meeting = []
# for _ in range(n):
#     s, e = map(int, input().split())
#     meeting.append((e, s))
# meeting.sort()
# print(meeting)
# answer = 0
# time = 0
# for m in meeting:
#     if m[1]>=time:
#         answer += 1
#         time = m[0]
# print(answer)