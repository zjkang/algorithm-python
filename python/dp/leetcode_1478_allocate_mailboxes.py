"""
author: Zhengjian Kang
date: 10/21/2021

残酷群每日一题: 10/20/2021

https://leetcode.com/problems/allocate-mailboxes/

1478. Allocate Mailboxes

note: 区间类第一种类型dp, dp[i][k]: 前i个元素拆分成k个空间的极值

Given the array houses and an integer k. where houses[i] is the location of the ith house along a street,
your task is to allocate k mailboxes in the street.

Return the minimum total distance between each house and its nearest mailbox.
The answer is guaranteed to fit in a 32-bit signed integer.

Example 1:
Input: houses = [1,4,8,10,20], k = 3
Output: 5
Explanation: Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 

Example 2:
Input: houses = [2,3,5,12,18], k = 2
Output: 9
Explanation: Allocate mailboxes in position 3 and 14.
Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.

Example 3:
Input: houses = [7,4,6,1], k = 1
Output: 8

Example 4:
Input: houses = [3,6,14,10], k = 4
Output: 0
 

Constraints:
n == houses.length
1 <= n <= 100
1 <= houses[i] <= 10^4
1 <= k <= n
Array houses contain unique integers.
"""

class Solution:
    def minDistance(self, houses: List[int], K: int) -> int:
        N = len(houses)
        houses.sort()
        houses.insert(0, -1)
        
        dp = [[float('inf')] * (K+1) for _ in range(N+1)] # dp[i][k]: first k houses with k mailboxes
        
        rang = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                total = 0
                for k in range(i, j + 1):
                    total += abs(houses[k] - houses[(i + j)//2])
                rang[i][j] = total
        
        for i in range(1, N + 1):
            dp[i][1] = rang[1][i]
            
        for i in range(1, N + 1):
            for k in range(2, K + 1):
                for j in range(1, i):
                    dp[i][k] = min(dp[i][k], dp[j][k-1] + rang[j+1][i])
        
        return dp[N][K]
