import sys
input = sys.stdin.readline().strip()
arr = list(input)
stack = []
op = []

for val in arr:
    if val == '(':
        stack.append(val)
        op.append(2)
        op.append(val)
        continue
    elif val == '[':
        stack.append(val)
        op.append(3)
        op.append(val)
        continue
    if len(stack) == 0:
        print(0)
        exit(0)
    if val == ')':
        last = stack.pop()
        if last == '[':
            print(0)
            exit(0)
        else:
            if op[-1] == '(':
                op.pop()
            else:
                op.append(val)

    if val == ']':
        last = stack.pop()
        if last == '(':
            print(0)
            exit(0)
        else:
            if op[-1] == '[':
                op.pop()
            else:
                op.append(val)

if len(stack) > 0 or len(op) == 0:
    print(0)
    exit(0)

for i, val in enumerate(op):
    if val == 2 or val == 3:
        if op[i-1] == 2 or op[i-1] == 3 or op[i-1] == ')' or op[i-1] == ']':
            stack.append('+')
        stack.append(val)
    if val == '(' or val == '[':
        stack.append('*')
        stack.append(val)
    if val == ')' or val == ']':
        stack.append(val)

del stack[0]


def priority(op):
    p = 0
    if op == '+':
        p = 1
    if op == '*':
        p = 2
    if op == '(' or op == '[':
        p = 3

    return p


post = []
temp = []
for val in stack:
    if val == 2 or val == 3:
        post.append(val)
    else:
        if val == ')' or val == ']':
            while temp[-1] != '(' and temp[-1] != '[':
                post.append(temp.pop())
            temp.pop()
        else:
            if len(temp) == 0:
                temp.append(val)
            else:
                if priority(val) > priority(temp[-1]):
                    temp.append(val)
                else:
                    if temp[-1] != '(' and temp[-1] != '[':
                        post.append(temp.pop())
                    temp.append(val)

while len(temp):
    last = temp.pop()
    if last == '*' or last == '+':
        post.append(last)


def calculate(a, b, op):
    if op == '+':
        return a + b
    else:
        return a * b


result = 0
for val in post:
    if val == 2 or val == 3:
        temp.append(val)
    else:
        pop1 = temp.pop()
        pop2 = temp.pop()
        cal = calculate(pop1, pop2, val)
        temp.append(cal)

print(temp[0])
