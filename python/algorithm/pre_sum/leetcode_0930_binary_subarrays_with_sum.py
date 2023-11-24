'''
author: Zhengjian Kang
date: 10/09/2021

残酷群每日一题: 10/09/2021

930. Binary Subarrays With Sum

https://leetcode.com/problems/binary-subarrays-with-sum/

note: prefix word freq count + hash

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

Constraints:
1 <= nums.length <= 3 * 10^4
nums[i] is either 0 or 1.
0 <= goal <= nums.length
'''

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count_map = defaultdict(int)
        count_map[0] = 1
        cur = 0
        res = 0
        for x in nums:
            cur += x
            res += count_map[cur - goal]
            count_map[cur] += 1
        return res
