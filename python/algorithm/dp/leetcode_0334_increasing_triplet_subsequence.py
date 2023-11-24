
"""
author: Zhengjian Kang
date: 03/08/2021

残酷群每日一题: 03/06/2021

https://leetcode.com/problems/increasing-triplet-subsequence/

334. Increasing Triplet Subsequence

note: LIS or maintain triplet variable to represent small, medium, large

Given an integer array nums, return true if there exists a triple of indices
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
1 <= nums.length <= 10^5
-231 <= nums[i] <= 231 - 1

"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False
        seq = []
        for n in nums:
            if not seq or n > seq[-1]:
                seq.append(n)
                if len(seq) >= 3:
                    return True
            else:
                idx = bisect.bisect_left(seq, n)
                seq[idx] = n
        return False
