"""
author: Zhengjian Kang
date: 03/25/2021

残酷群每日一题: 01/21/2021

https://leetcode.com/problems/first-missing-positive/

41. First Missing Positive

note: index sort

Given an unsorted integer array nums, find the smallest missing positive
integer.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
0 <= nums.length <= 300
-2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        i, n = 0, len(nums)
        while i < n:
            while nums[i] >= 1 and nums[i] <= n and nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
                j = nums[i]-1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                return i+1
            i += 1
        return n+1
