"""
author: Zhengjian Kang
date: 10/26/2021

残酷群每日一题: 10/26/2021

https://leetcode.com/problems/kth-smallest-subarray-sum/

1918. Kth Smallest Subarray Sum

note: binary search by value, and two pointers

Given an integer array nums of length n and an integer k, return the kth smallest subarray sum.

A subarray is defined as a non-empty contiguous sequence of elements in an array.
A subarray sum is the sum of all elements in the subarray.

Example 1:
Input: nums = [2,1,3], k = 4
Output: 3
Explanation: The subarrays of [2,1,3] are:
- [2] with sum 2
- [1] with sum 1
- [3] with sum 3
- [2,1] with sum 3
- [1,3] with sum 4
- [2,1,3] with sum 6 
Ordering the sums from smallest to largest gives 1, 2, 3, 3, 4, 6. The 4th smallest is 3.

Example 2:
Input: nums = [3,3,5,5], k = 7
Output: 10
Explanation: The subarrays of [3,3,5,5] are:
- [3] with sum 3
- [3] with sum 3
- [5] with sum 5
- [5] with sum 5
- [3,3] with sum 6
- [3,5] with sum 8
- [5,5] with sum 10
- [3,3,5], with sum 11
- [3,5,5] with sum 13
- [3,3,5,5] with sum 16
Ordering the sums from smallest to largest gives 3, 3, 5, 5, 6, 8, 10, 11, 13, 16. The 7th smallest is 10.
 

Constraints:
n == nums.length
1 <= n <= 2 * 10^4
1 <= nums[i] <= 5 * 10^4
1 <= k <= n * (n + 1) / 2
"""

class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def count_smaller_or_equal(t, presum): # O(n)
            j = 0
            n = len(presum)
            ret = 0
            for i in range(n):
                while j < n and presum[j] - presum[i] <= t:
                    j += 1
                ret += j-i-1
            return ret
            
        presum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            presum[i+1] = presum[i] + nums[i]
        
        left, right = 0, presum[-1] - presum[0]
        while left < right:
            mid = left + (right - left) // 2
            count = count_smaller_or_equal(mid, presum) # of diff <= mid
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left
