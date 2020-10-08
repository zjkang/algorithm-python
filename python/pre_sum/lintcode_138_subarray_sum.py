"""
author: Wei Li
date: 10/08/2020

https://www.lintcode.com/problem/subarray-sum/note/228582

138. Subarray Sum

Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

样例
Example 1:

Input:  [-3, 1, 2, -3, 4]
Output: [0, 2] or [1, 3].
Explanation: return anyone that the sum is 0.
Example 2:

Input:  [-3, 1, -4, 2, -3, 4]
Output: [1,5]	
注意事项
There is at least one subarray that it's sum equals to zero.
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        pre_sum_mapping = {0: 0}
        
        pre_sum = 0
        for i, num in enumerate(nums):
            pre_sum += num
            
            if pre_sum in pre_sum_mapping:
                return [pre_sum_mapping[pre_sum], i]
                
        
            pre_sum_mapping[pre_sum] = i + 1
        
        return [-1, -1]    
        