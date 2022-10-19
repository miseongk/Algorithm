import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(0, n + 1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b, x):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if x == 1:
        if a == b:
            print("YES")
        else:
            print("NO")
    else:
        if a < b:
            parent[b] = a
        else: 
            parent[a] = b

for _ in range(m):
    x, a, b = map(int, input().split())
    union_parent(parent, a, b, x)
