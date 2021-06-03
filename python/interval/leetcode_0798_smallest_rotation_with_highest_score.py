'''
author: Zhengjian Kang
date: 06/03/2021

残酷群每日一题: 06/01/2021

https://leetcode.com/problems/smallest-rotation-with-highest-score/

798. Smallest Rotation with Highest Score

note: 这道题很难看出是查分数组的pattern。难点在于用几个例子分析，分析一个具体的数在左移的过程中的值的变化，e.g., 111000111，来寻求可能的pattern

Given an array nums, we may rotate it by a non-negative integer k so that the array
becomes nums[k], nums[k+1], nums[k+2], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1].
Afterward, any entries that are less than or equal to their index are worth 1 point.

For example, if we have [2, 4, 1, 3, 0], and we rotate by k = 2, it becomes [1, 3, 0, 2, 4].
This is worth 3 points because 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].

Over all possible rotations, return the rotation index k that corresponds to the highest score we could receive.
If there are multiple answers, return the smallest such index k.

Example 1:
Input: [2, 3, 1, 4, 0]
Output: 3
Explanation:  
Scores for each k are listed below: 
k = 0,  nums = [2,3,1,4,0],    score 2
k = 1,  nums = [3,1,4,0,2],    score 3
k = 2,  nums = [1,4,0,2,3],    score 3
k = 3,  nums = [4,0,2,3,1],    score 4
k = 4,  nums = [0,2,3,1,4],    score 3
So we should choose k = 3, which has the highest score.

Example 2:
Input: [1, 3, 0, 2, 4]
Output: 0
Explanation: nums will always have 3 points no matter how it shifts.
So we will choose the smallest k, which is 0.
Note:

nums will have length at most 20000.
nums[i] will be in the range [0, nums.length].
'''

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        # diff array
        # https://github.com/wisdompeak/LeetCode/tree/master/Others/798.Smallest-Rotation-with-Highest-Score
        N = len(nums)
        diff = [0] * N
        for i in range(N):
            if nums[i] <= i:
                diff[0] += 1
                diff[(i-nums[i]+1)%N] -= 1
                diff[(i+1)%N] += 1
            else:
                diff[(i+1)%N] += 1
                diff[(i+1 + N-nums[i])% N] -= 1
        
        count, ret = 0, 0
        k = 0
        for i in range(N):
            count += diff[i]
            if count > ret:
                ret = count
                k = i
        return k
