from bisect import bisect_left, bisect_right

n = int(input())
card = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

def count_range(array, x):
    left_value = bisect_left(array, x)
    right_value = bisect_right(array, x)
    return right_value - left_value

card.sort()

for i in c:
    print(count_range(card, i), end=' ')
