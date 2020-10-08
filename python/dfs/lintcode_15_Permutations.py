"""
author: Wei Li
date: 10/08/2020

https://www.lintcode.com/problem/permutations/description?_from=ladder&&fromId=161

15. Permutations

Given a list of numbers, return all possible permutations.

样例
Example 1:

Input: [1]
Output:
[
  [1]
]
Example 2:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
Challenge
Do it without recursion.

Constaints
You can assume that there is no duplicate numbers in the list.
"""
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        nums.sort()
        
        ans = []
        self.helper(nums, [], ans)
        
        return ans

    def helper(self, nums, formed, ans):
        if len(nums) == 0:
            ans.append(formed[:])
            return
        
        for i in range(len(nums)):
            formed.append(nums[i])
            self.helper(nums[:i] + nums[i + 1:], formed, ans)
            formed.pop()
        
 """
 BFS approach 
 """       
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        nums.sort()
        stack = [[num] for num in nums]
        
        ans = []
        while stack:
            last = stack.pop()
            
            if len(last) == len(nums):
                ans.append(last)
                continue
            
            for n in nums:
                if n not in last:
                    stack.append(last + [n])
        
        return ans      