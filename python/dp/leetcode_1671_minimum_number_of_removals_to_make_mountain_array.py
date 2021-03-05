
"""
author: Zhengjian Kang
date: 03/04/2021

残酷群每日一题: 02/28/2021

https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

1671. Minimum Number of Removals to Make Mountain Array

note: LIS问题 + two pass

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to
remove to make nums​​​ a mountain array.

Example 1:
Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to
remove any elements.

Example 2:
Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5,
making the array nums = [1,5,6,3,1].

Example 3:
Input: nums = [4,3,2,1,1,2,3,1]
Output: 4

Example 4:
Input: nums = [1,2,3,4,4,3,2,1]
Output: 1

Constraints:
3 <= nums.length <= 1000
1 <= nums[i] <= 10^9
It is guaranteed that you can make a mountain array out of nums.
"""


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        m = len(nums)
        left_to_right = self.cal_lis(nums)
        right_to_left = self.cal_lis(nums[::-1])
        right_to_left = right_to_left[::-1]

        res = float('inf')
        for i in range(1, m-1):
            if left_to_right[i] > 1 and right_to_left[i] > 1:
                res = min(res, m - left_to_right[i] - right_to_left[i] + 1)
        return res

    # calculate lis (longest increasing subsequence)
    def cal_lis(self, nums):
        inc = []
        dp = [1] * len(nums)
        for i in range(len(nums)):
            pos = bisect.bisect_left(inc, nums[i])
            dp[i] = pos + 1
            if pos == len(inc):
                inc.append(nums[i])
            else:
                inc[pos] = nums[i]
        return dp
