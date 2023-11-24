
"""
author: Zhengjian Kang
date: 02/24/2021

https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

862. Shortest Subarray with Sum at Least K

Return the length of the shortest, non-empty, contiguous subarray of A
with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

Example 1:
Input: A = [1], K = 1
Output: 1

Example 2:
Input: A = [1,2], K = 4
Output: -1

Example 3:
Input: A = [2,-1,2], K = 3
Output: 3

Note:
1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
"""


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # pre-fix sum using monotonic deque
        m = len(A)
        pre_sum = [0] * m
        for i in range(m):
            pre_sum[i] = A[i] + (0 if i == 0 else pre_sum[i-1])
        # increasing deque
        stack = collections.deque([])
        res = float('inf')
        for idx, val in enumerate(pre_sum):
            if val >= K:
                res = min(res, idx+1)
            # search shortest subarray
            while stack and val - stack[0][1] >= K:
                res = min(res, idx - stack[0][0])
                stack.popleft()
            # maintain monotonic deque
            while stack and stack[-1][1] >= val:
                stack.pop()
            stack.append((idx, val))
        return -1 if res == float('inf') else res
