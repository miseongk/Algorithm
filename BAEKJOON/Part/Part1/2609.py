n, m = map(int, input().split())


def gcd(n, m):
    while n != m:
        if n > m:
            n -= m
        else:
            m -= n

    return n


def lcm(n, m):
    num = gcd(n, m)

    return n//num * m//num * num


print(gcd(n, m))
print(lcm(n, m))
