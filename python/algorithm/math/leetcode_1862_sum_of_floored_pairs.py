'''
author: Zhengjian Kang
date: 05/19/2021

残酷群每日一题: 05/19/2021

https://leetcode.com/problems/sum-of-floored-pairs/

1862. Sum of Floored Pairs

Given an integer array nums, return the sum of floor(nums[i] / nums[j]) for all pairs of
indices 0 <= i, j < nums.length in the array. Since the answer may be too large, return it modulo 109 + 7.

The floor() function returns the integer part of the division.

Example 1:
Input: nums = [2,5,9]
Output: 10
Explanation:
floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
floor(5 / 2) = 2
floor(9 / 2) = 4
floor(9 / 5) = 1
We calculate the floor of the division for every pair of indices in the array then sum them up.

Example 2:
Input: nums = [7,7,7,7,7,7,7]
Output: 49
 
Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
'''

class Solution:
    # note:
#     首先，题目中计算任意两个元素之间的floor div，意味着数组里面的元素顺序并没有任何意义。我们可以任意选定一个元素i作为分母，考虑其他元素j做分子进行除法的结果。

# 显然，对于比nums[i] = x小的元素做分子，结果都是零，没有意义。我们只关心那些比x大的元素。我们知道，数值位于区间[x*k, x*(k+1)-1]的元素作为分子，除法的结果就是k（k=1,2,3...）。自然地我们想知道数值位于该区间的元素多少？我们发现数组元素的数值大小的上限是100000，联想到桶排序，我们只需预处理每个数组元素s，将其出现的频次统计在count[s]里。如果想知道大小位于某个区间内的元素的频次和，只需要用count的前缀和数组presum即可。

# 综上，对于x，我们从小到大遍历所有的k。c = presum[x*(k+1)-1] - presum[x*k-1]代表了有多少元素与x的商恰好是k，最终答案就可以加上c*k. 特别注意，k的遍历的上界可能会使得x*(k+1)-1超过100000（桶的个数）。所以最后一段区间是一个“零头”，需要单独处理[x*k, 100000]。

    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        max_n = max(nums)
        # bucket sort counter
        count = [0] * (max_n+1)
        for x in nums:
            count[x] += 1
        # prefix sum
        pre_sum = [0] * (max_n+1)
        for i in range(1, max_n+1):
            pre_sum[i] = pre_sum[i-1] + count[i]
            
        visited = set()
        ret = 0
        MOD = 10**9+7
        
        for x in nums:
            if x in visited: continue
            ans = 0
            k = 1
            while x*k+x-1 <= max_n:
                ans += (pre_sum[x*k+x-1] - pre_sum[x*k-1]) * k
                k += 1

            if x*k+x-1 > max_n:
                ans += (pre_sum[max_n] - pre_sum[x*k-1]) * k
            
            ret += ans * count[x]
            visited.add(x)
        
        return ret % MOD

