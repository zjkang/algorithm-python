'''
author: Zhengjian Kang
date: 10/08/2021

残酷群每日一题: 10/07/2021

2025. Maximum Number of Ways to Partition an Array

https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

note: prefix + suffix + hash 记录<key, value>: {prefix-sum: freq}

You are given a 0-indexed integer array nums of length n.
The number of ways to partition nums is the number of pivot indices that satisfy both conditions:

1 <= pivot < n
nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]
You are also given an integer k. You can choose to change the value of one element of nums to k, or to leave the array unchanged.

Return the maximum possible number of ways to partition nums to satisfy both conditions after changing at most one element.

Example 1:
Input: nums = [2,-1,2], k = 3
Output: 1
Explanation: One optimal approach is to change nums[0] to k. The array becomes [3,-1,2].
There is one way to partition the array:
- For pivot = 2, we have the partition [3,-1 | 2]: 3 + -1 == 2.

Example 2:
Input: nums = [0,0,0], k = 1
Output: 2
Explanation: The optimal approach is to leave the array unchanged.
There are two ways to partition the array:
- For pivot = 1, we have the partition [0 | 0,0]: 0 == 0 + 0.
- For pivot = 2, we have the partition [0,0 | 0]: 0 + 0 == 0.

Example 3:
Input: nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33
Output: 4
Explanation: One optimal approach is to change nums[2] to k. The array becomes [22,4,-33,-20,-15,15,-16,7,19,-10,0,-13,-14].
There are four ways to partition the array.

Constraints:
n == nums.length
2 <= n <= 10^5
-105 <= k, nums[i] <= 10^5

'''

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = sum(nums)
        
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i-1] + nums[i]
        
        suf = [0] * n
        suf[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1] + nums[i]
        
        res0 = 0
        for i in range(n-1):
            if pre[i] == total - pre[i]:
                res0 += 1
        
        res = [0] * n
        
        count = defaultdict(int)
        for i in range(n):
            new_total = total + k - nums[i]
            if new_total % 2 == 0:
                res[i] += count[new_total//2]
            count[pre[i]] += 1
    
        count = defaultdict(int)
        for i in range(n-1,-1,-1):
            new_total = total + k - nums[i]
            if i == 2:
                print(new_total, count)
            if new_total % 2 == 0:
                res[i] += count[new_total//2]
            count[suf[i]] += 1
        
        return max(res0, max(res))
