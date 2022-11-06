from collections import deque

def solution(stones, k):
    window = deque()
    out = []
    
    for i, stone in enumerate(stones):
        while window and stones[window[-1]] < stone:
            window.pop()

        window.append(i)
        
        if window[0] == i - k:
            window.popleft()
        if i >= k - 1:
            out.append(stones[window[0]])
            
    return min(out)

# [참고] - https://leetcode.com/problems/sliding-window-maximum/discuss/237611/Simplest-O(n)-Python-Solution-with-Explanation
# https://velog.io/@corone_hi/75.-Sliding-Window-Maximum
    

#     for i in range(len(stones)):
#         end = i
#         sum_num += stones[end]
#         if end - start < k - 1:
#             continue
#         elif end - start > k - 1:
#             sum_num -= stones[start]
#             start += 1
#         num.append(max(stones[start:end+1]))
    
#     answer = min(num)  