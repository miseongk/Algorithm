def solution(price, money, count):
    sum = 0
    for i in range(1, count+1):
        sum += i
    need = price * sum - money

    return need if need > 0 else 0 
