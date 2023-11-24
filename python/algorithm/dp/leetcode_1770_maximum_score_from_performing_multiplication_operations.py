
"""
author: Zhengjian Kang
date: 02/25/2021

残酷群每日一题: 02/25/2021

https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

1770. Maximum Score from Performing Multiplication Operations

note: 区间dp，这道题的区间选择的前几个和后几个

You are given two integer arrays nums and multipliers of size n and m
respectively, where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations.
On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.

Example 1:
Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.

Example 2:
Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score.
The total score is 50 + 15 - 9 + 4 + 42 = 102.

Constraints:
n == nums.length
m == multipliers.length
1 <= m <= 10^3
m <= n <= 10^5
-1000 <= nums[i], multipliers[i] <= 1000
"""


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        # max value when picking first i, last j elements
        dp = [[float('-inf')] * (m+1) for _ in range(m+1)]
        res = float('-inf')
        for i in range(m+1):
            for j in range(m-i+1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + nums[n-j] * multipliers[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + nums[i-1] * multipliers[i+j-1]
                else:
                    dp[i][j] = max(
                        dp[i-1][j] + nums[i-1] * multipliers[i+j-1],
                        dp[i][j-1] + nums[n-j] * multipliers[i+j-1])
                if i+j == m:
                    res = max(res, dp[i][j])
        return res
