"""
author: Zhengjian Kang
date: 02/12/2021

残酷群每日一题: 02/08/2021

https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

1749. Maximum Absolute Sum of Any Subarray

note: subarray sum的问题可以考虑利用
1. pre-fix sum的性质 prefix_sum[i] - prefix_sum[j], prefix_sum[0] = 0
2. max subarray sum - dp的方法，继承，另起炉灶


You are given an integer array nums. The absolute sum of a subarray
[numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1
+ numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:
If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.

Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:
Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""


class Solution1:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # maximum subarray sum - dp
        res = 0
        pre_sum = 0
        max_sum = 0
        min_sum = 0
        for n in nums:
            pre_sum += n
            max_sum = max(max_sum, pre_sum)
            min_sum = min(min_sum, pre_sum)
        return max_sum - min_sum


class Solution2:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = 0
        pre_sum = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        for n in nums:
            pre_sum += n
            res = max(res, abs(pre_sum))
            if max_sum != float('-inf'):
                res = max(res, abs(pre_sum - max_sum))
            max_sum = max(max_sum, pre_sum)
            if min_sum != float('inf'):
                res = max(res, abs(pre_sum - min_sum))
            min_sum = min(min_sum, pre_sum)
        return res


class Solution3:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pre_sum = 0
        max_sum = 0
        min_sum = 0  # include no element
        for n in nums:
            pre_sum += n
            max_sum = max(pre_sum, max_sum)
            min_sum = min(pre_sum, min_sum)
        return max_sum - min_sum
