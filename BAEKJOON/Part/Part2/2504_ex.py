# [참고]
# 재귀 사용
def func(p):
    if len(p) == 0:
        return 1
    dic = {'(': ')', '[': ']'}
    ans, sub, stack = 0, '', []
    for i in p:
        sub += i
        if len(stack) > 0 and dic.get(stack[-1], '') == i:
            stack.pop()
        else:
            stack.append(i)
        if len(stack) == 0:
            ans, sub = ans + func(sub[1:-1]) * (2 if sub[0] == '(' else 3), ''
    if len(stack) > 0:
        return 0
    return ans


print(func(input()))
