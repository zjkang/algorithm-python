"""
author: Zhengjian Kang
date: 08/20/2021
残酷群每日一题: 08/20/2021

https://leetcode.com/problems/longest-increasing-subsequence/
300. Longest Increasing Subsequence

note: LIS

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some
or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
 
Constraints:
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for n in nums:
            if not lis or n > lis[-1]:
                lis.append(n)
            else:
                pos = bisect.bisect_left(lis, n)
                lis[pos] = n
        return len(lis)
 
