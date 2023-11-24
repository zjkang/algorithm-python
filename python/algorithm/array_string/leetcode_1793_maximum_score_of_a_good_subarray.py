
"""
author: Zhengjian Kang
date: 03/16/2021

残酷群每日一题: 03/16/2021

https://leetcode.com/problems/maximum-score-of-a-good-subarray/

1793. Maximum Score of a Good Subarray

note:做题的联想到这道题等价最大矩形,用单调栈解的问题。后来听了群主的方法后，发现可以使用
two pointers向两边扩展

You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ...,
nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray

Example 1:
Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of
min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15.

Example 2:
Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) *
(4-0+1) = 4 * 5 = 20.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 2 * 10^4
0 <= k < nums.length
"""


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # two pointers: https://www.youtube.com/watch?v=OcqPeux47fU
        n = len(nums)
        l, r = k, k
        min_val = nums[k]

        res = 0
        while l >= 0 or r < n:
            while l >= 0 and nums[l] >= min_val:
                l -= 1
            while r < n and nums[r] >= min_val:
                r += 1

            res = max(res, min_val * (r-l-1))
            min_val = max(nums[l] if l >= 0 else float(
                '-inf'), nums[r] if r < n else float('-inf'))

        return res


class Solution2:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res = 0
        stack = [0]
        i = 1
        nums.insert(0, -1)
        k = k + 1
        while i < len(nums):
            while stack and nums[stack[-1]] > nums[i]:
                left_idx = stack.pop()
                if i > k and stack[-1]+1 <= k:
                    res = max(res, (i - stack[-1]-1) * nums[left_idx])
            if not stack or nums[i] >= nums[stack[-1]]:
                stack.append(i)
            i += 1
        while len(stack) > 1:
            left_idx = stack.pop()
            if stack[-1]+1 <= k:
                res = max(res, (len(nums) - stack[-1]-1) * nums[left_idx])
        return res
