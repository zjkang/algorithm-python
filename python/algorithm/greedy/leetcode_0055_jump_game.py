
"""
author: Zhengjian Kang
date: 03/24/2021

残酷群每日一题: 03/24/2021

https://leetcode.com/problems/jump-game/

55. Jump Game

note: greedy搜寻最大值

Given an array of non-negative integers nums, you are initially positioned at
the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what.
Its maximum jump length is 0, which makes it impossible to reach the last
index.

Constraints:
1 <= nums.length <= 3 * 10^4
0 <= nums[i] <= 10^5

"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, max_pos, n = 0, 0, len(nums)
        while i <= max_pos and i < n:
            max_pos = max(max_pos, i + nums[i])
            if max_pos >= n-1:
                return True
            i += 1
        return False
