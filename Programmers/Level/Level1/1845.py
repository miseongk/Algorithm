def solution(nums):
    answer = 0
    n = len(nums)
    nums = set(nums)
    if len(nums) >= n/2:
        answer = n/2
    else:
        answer = len(nums)
    return answer

# [참고]
# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))
