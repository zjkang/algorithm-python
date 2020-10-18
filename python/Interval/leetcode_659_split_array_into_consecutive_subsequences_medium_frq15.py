"""
author: Wei Li
date: 10/17/2020

https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

452. Minimum Number of Arrows to Burst Balloons

Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:
Input: [1,2,3,4,4,5]
Output: False
 
Constraints:

1 <= nums.length <= 10000
"""
# Greedy

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = collections.Counter(nums)
        tails = collections.Counter()
        for num in nums:
            if count[num] == 0:
                continue
            elif tails[num] > 0:
                tails[num] -= 1
                tails[num + 1] += 1
            elif count[num + 1] > 0 and count[num + 2] > 0:
                count[num + 1] -= 1
                count[num + 2] -= 1
                tails[num + 3] += 1
            else:
                return False
            count[num] -= 1
        return True