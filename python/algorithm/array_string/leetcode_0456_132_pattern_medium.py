"""
author: Zhengjian Kang
date: 10/23/2020

https://leetcode.com/problems/132-pattern/

456. 132 Pattern

Given an array of n integers nums, a 132 pattern is a subsequence of three
integers nums[i], nums[j] and nums[k] such that i < j < k and
nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or
the O(n) solution?


Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2],
[-1, 3, 0] and [-1, 2, 0].

Constraints:

n == nums.length
1 <= n <= 104
-109 <= nums[i] <= 109
"""


class Solution:
    # https://www.cnblogs.com/grandyang/p/6081984.html
    def find132pattern(self, nums: List[int]) -> bool:
        n, mn = len(nums), float('inf')
        for j in range(n):
            mn = min(mn, nums[j])
            if mn == nums[j]:
                continue
            for k in range(n-1, j, -1):
                if mn < nums[k] < nums[j]:
                    return True
        return False
