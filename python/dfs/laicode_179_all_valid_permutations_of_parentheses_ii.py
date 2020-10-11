"""
author: Zhengjian Kang
date: 10/10/2020

https://app.laicode.io/app/problem/179

179. All Valid Permutations Of Parentheses II

Get all valid permutations of l pairs of (), m pairs of <> and n pairs of {}.

Assumptions

l, m, n >= 0
l + m + n > 0
Examples

l = 1, m = 1, n = 0, all the valid permutations are ["()<>", "(<>)", "<()>", "<>()"]
"""


class Solution(object):
 def validParentheses(self, l, m, n):
   """
   input: int l, int m, int n
   return: string[]
   """
   self.result = []
   self.paren = ['(', ')', '<', '>', '{', '}']
   self.total = 2 * (l + m + n)
   self.dfs([l, l, m, m, n, n], [], [])
   return self.result

  def dfs(self, remain, stack, one_res):
   '''
   remain: remaining
   stack: keep stack of left parentheis
   one_res: one result
   '''
   if len(one_res) == self.total:
     self.result.append("".join(one_res))
     return
  
   for index, n in enumerate(remain):
     if index % 2 == 0:
       if n > 0:
         one_res.append(self.paren[index])
         remain[index] -= 1
         stack.append(self.paren[index])
         self.dfs(remain, stack, one_res)
         one_res.pop()
         remain[index] += 1
         stack.pop()
     elif len(stack) and stack[-1] == self.paren[index-1]:
       one_res.append(self.paren[index])
       remain[index] -= 1
       stack.pop()
       self.dfs(remain, stack, one_res)
       one_res.pop()
       remain[index] += 1
       stack.append(self.paren[index-1])
