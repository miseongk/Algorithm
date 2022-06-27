n = int(input())
array = list(map(int, input().split()))

d = []
# 양수일 때 flag = 1
if array[0] >= 0:
    flag = 1
else:
    flag = 0
d.append(array[0])
i = 1
j = 0
while i < n:
    # 양수일 때
    if array[i] >= 0:
        # d에 들어가있는 숫자가 음수이면
        if flag == 0:
            # 뒤로 한 칸 이동 후 flag 양수로 변경
            j += 1
            flag = 1
            d.append(0)
    else:
        if flag == 1:
            j += 1
            flag = 0
            d.append(0)
    d[j] += array[i]
    i += 1

for i in range(1, len(d)):
    if d[i] < d[i-1] + d[i]:
        d[i] += d[i-1]

if len(d) == 1 and d[0] < 0:
    print(max(array))
else:
    print(max(d))


# example
# n = int(input())
# array = list(map(int, input().split()))
#
# max = array[0]
# sum = 0
# for i in range(0, n):
#     sum += array[i]
#     if max < sum:
#         max = sum
#     if sum < 0:
#         sum = 0
#
# print(max)
