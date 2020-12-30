"""
author: Zhengjian Kang
date: 10/09/2020

https://leetcode.com/problems/partition-equal-subset-sum/

416. Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp[i][j]: able to use the first i elements to sum up to j
        # dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        half_sum = total_sum // 2
        m = len(nums)
        dp = [[False] * (total_sum + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            for j in range(1, total_sum + 1):
                dp[i][j] = dp[i-1][j]
                if not dp[i][j] and j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j-nums[i-1]]
                if dp[i][half_sum]:
                    return True
        return False


def canPartition(self, nums: List[int]) -> bool:
    # dp[i][j]: able to use the first i elements to sum up to j
    # dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    half_sum = total_sum // 2
    dp = [False] * (total_sum + 1)
    dp[0] = True
    for num in nums:
        for i in range(total_sum, -1, -1):
            if dp[i] and i + num <= total_sum:
                dp[i + num] = True
            if dp[half_sum]:
                return True
    return False
