"""
author: Zhengjian Kang
date: 11/30/2020

https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

1658. Minimum Operations to Reduce X to Zero

You are given an integer array nums and an integer x. In one operation,
you can either remove the leftmost or the rightmost element from the array
nums and subtract its value from x. Note that this modifies the array for
future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's
possible, otherwise, return -1.

Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce
x to zero.

Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and
the first two elements (5 operations in total) to reduce x to zero.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
"""


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        remain = total_sum - x
        count = self.subarray_sum(nums, remain)
        return -1 if count == -1 else len(nums) - count

    def subarray_sum(self, nums, target):
        if target == 0:
            return 0
        map = {0: -1}
        acc_sum = 0
        max_dist = -1
        for i in range(len(nums)):
            acc_sum += nums[i]
            if acc_sum - target in map:
                max_dist = max(max_dist, i - map[acc_sum - target])
            map[acc_sum] = i
        return max_dist
