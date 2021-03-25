"""
author: Zhengjian Kang
date: 03/25/2021

残酷群每日一题: 01/03/2021

https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

1712. Ways to Split Array Into Three Subarrays

note: two pointers + binary search

A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays - named left,
mid, right respectively from left to right.
The sum of the elements in left is less than or equal to the sum of the
elements in mid, and the sum of the elements in mid is less than or equal
to the sum of the elements in right.
Given nums, an array of non-negative integers, return the number of good
ways to split nums. As the number may be too large, return it modulo 109 + 7.

Example 1:
Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].

Example 2:
Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]

Example 3:
Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.

Constraints:
3 <= nums.length <= 10^5
0 <= nums[i] <= 10^4
"""


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        m = len(nums)
        pre_sum = [0] * m
        pre_sum[0] = nums[0]
        for i in range(1, m):
            pre_sum[i] = pre_sum[i-1] + nums[i]
        post_sum = [0] * m
        post_sum[-1] = nums[-1]
        for i in range(m-2, -1, -1):
            post_sum[i] = post_sum[i+1] + nums[i]

        res = 0
        for i in range(m-2):
            first = pre_sum[i]
            left = self.find_left_bound(pre_sum, first*2, i+1, m-1)
            if left == -1:
                break
            right = self.find_right_bound(post_sum, i+1, m-1)
            if right == -1:
                break
            if right > left:
                res = (res + right - left) % (10**9 + 7)
        return res

    def find_left_bound(self, pre_sum, target, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if pre_sum[mid] >= target:
                end = mid
            else:
                start = mid
        if pre_sum[start] >= target:
            return start
        if pre_sum[end] >= target:
            return end
        return -1

    def find_right_bound(self, post_sum, start, end):
        total = post_sum[start]
        while start + 1 < end:
            mid = (start + end) // 2
            if post_sum[mid] >= total - post_sum[mid]:
                start = mid
            else:
                end = mid
        if post_sum[end] >= total - post_sum[end]:
            return end
        if post_sum[start] >= total - post_sum[start]:
            return start
        return -1
