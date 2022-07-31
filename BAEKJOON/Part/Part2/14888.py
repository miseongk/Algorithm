# 코드 참고 함. 너무 어렵다...

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

min = int(1e9)
max = int(-1e9)


def dfs(depth, result):
    global max
    global min
    backup = result
    if depth == len(num):
        if result > max:
            max = result
        if result < min:
            min = result
        return

    for i in range(4):
        if op[i] > 0:
            op[i] -= 1

            result = calculate(result, num[depth], i)
            dfs(depth+1, result)
            result = backup
            op[i] += 1


def calculate(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        if a < 0:
            return (-1)*((-1)*a//b)
        else:
            return a//b


dfs(1, num[0])

print(max)
print(min)
