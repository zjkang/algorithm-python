"""
author: Wei Li
date: 10/09/2020

https://leetcode.com/problems/product-of-array-except-self/

238.  Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or
suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not
count as extra space for the purpose of space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        N = len(nums)
        ans = [0] * N

        ans[0] = 1
        for i in range(1, N):
            ans[i] = nums[i - 1] * ans[i - 1]

        R = 1
        for i in range(N - 1, -1, -1):
            ans[i] = ans[i] * R
            R *= nums[i]

        return ans
