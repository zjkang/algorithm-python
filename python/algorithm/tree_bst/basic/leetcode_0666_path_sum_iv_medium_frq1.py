"""
author: Wei Li
date: 10/15/2020

https://leetcode.com/problems/path-sum-iv/

666. Path Sum IV

If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:

The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.

It's guaranteed that the given list represents a valid connected binary tree.

Example 1:
Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.
 

Example 2:
Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.
""" 
# Recursion
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        self.ans = 0
        values = {x // 10: x % 10 for x in nums}
        
        def dfs(node, running_sum = 0):
            if node not in values: return
            
            running_sum += values[node]
            
            depth, pos = divmod(node, 10)
            
            left = (depth + 1) * 10 + 2 * pos - 1
            right = left + 1
            
            if left not in values and right not in values:
                self.ans += running_sum
            else:
                dfs(left, running_sum)
                dfs(right, running_sum)
        
        dfs(nums[0] // 10)
        
        return self.ans
 
 # Kang's solution
 class Solution:
    def pathSum(self, nums: List[int]) -> int:
        self.total = 0
        num_map = {}
        for n in nums:
            num_map[(n // 100, n // 10 % 10)] = n % 10
        self.dfs(num_map, 1, 1, 0)
        return self.total
        
    def dfs(self, num_map, depth, pos, cur):
        if (depth, pos) not in num_map: return
        cur += num_map[(depth, pos)]
        if self.is_leaf(num_map, depth, pos):
            self.total += cur
            return
        self.dfs(num_map, depth+1, pos*2-1, cur)
        self.dfs(num_map, depth+1, pos*2, cur)
        
    def is_leaf(self, num_map, depth, pos):
        return (depth+1, pos*2-1) not in num_map and (depth+1, pos*2) not in num_map
        