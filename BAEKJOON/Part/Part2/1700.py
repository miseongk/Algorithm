n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
tap = []

for idx, a in enumerate(arr):
    change_idx = -1
    change_val = -1
    del_idx = -1
    if a in tap:
        continue
    else:
        # 멀티탭이 꽉 차 있는 경우
        if len(tap) == n:
            for t_idx, t in enumerate(tap):
                # 1. 현재부터 사용하지 않는 전기용품의 경우
                if t not in arr[idx:]:
                    del_idx = t_idx
                    break
                # 2. 가장 멀리 있는 경우
                else:
                    cur_idx = arr[idx:].index(t)
                    if change_idx < cur_idx:
                        change_idx = cur_idx
                        change_val = t
                        del_idx = t_idx

            del tap[del_idx]
            result += 1
            tap.append(a)
        else:
            tap.append(a)

print(result)
