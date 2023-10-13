def solution(name):
    return straight(name) + horizon(name)


# 알파벳을 A로 맞추기 위해 위, 아래로 움직이는 횟수 구하기
def straight(name):
    answer = 0
    for val in name:
        cnt = min(abs(ord("A") - ord(val)), abs(ord("Z") - ord(val) + 1))
        answer += cnt

    return answer


# 왼쪽, 오른쪽으로 최소로 움직이는 횟수 구하기
def horizon(name):
    min_value = int(1e9)
    # 오른쪽으로만 가는 경우
    cnt = cal(name)
    if cnt == 0:
        return 0
    min_value = min(min_value, cnt)

    # 오른쪽으로 갔다가 왼쪽으로 가는 경우
    for i in range(len(name) // 2 + 1):
        split = name[i:]
        reverse_split = split[::-1]
        cnt = cal(reverse_split) + (i - 1) * 2
        if i == 0:
            cnt += 2
        min_value = min(min_value, cnt)

    # 왼쪽으로 갔다가 오른쪽으로 가는 경우
    reverse_name = name[::-1]
    for i in range(len(reverse_name) // 2 + 1):
        split = reverse_name[i:]
        reverse_split = split[::-1]
        cnt = cal(reverse_split) + (i - 1) * 2 + 1
        min_value = min(min_value, cnt)

    return min_value


# 순회하면서 마지막에 A가 연속으로 나오는 횟수를 구해 그 전까지 이동하는 횟수 구하기
def cal(name):
    flag = 0
    cnt = 0
    for val in name:
        cnt += 1
        if val == "A":
            flag += 1
        else:
            flag = 0
    if flag > 0:
        cnt -= flag
    return cnt
