"""
author: Zhengjian Kang
date: 10/04/2021

残酷群每日一题: 10/02/2021
https://leetcode.com/problems/the-score-of-students-solving-math-expression/

2019. The Score of Students Solving Math Expression
note: 241 Different Ways to Add Parentheses & 227 Basic Calculator II的结合

You are given a string s that contains digits 0-9, addition symbols '+', and multiplication symbols '*' only,
representing a valid math expression of single digit numbers (e.g., 3+5*2).
This expression was given to n elementary school students. The students were instructed to
get the answer of the expression by following this order of operations:

Compute multiplication, reading from left to right; Then,
Compute addition, reading from left to right.
You are given an integer array answers of length n, which are the submitted answers of the students
in no particular order. You are asked to grade the answers, by following these rules:

If an answer equals the correct answer of the expression, this student will be rewarded 5 points;
Otherwise, if the answer could be interpreted as if the student applied the operators in the wrong order
but had correct arithmetic, this student will be rewarded 2 points;
Otherwise, this student will be rewarded 0 points.
Return the sum of the points of the students.

Example 1:
Input: s = "7+3*1*2", answers = [20,13,42]
Output: 7
Explanation: As illustrated above, the correct answer of the expression is 13, therefore one student is rewarded 5 points: [20,13,42]
A student might have applied the operators in this wrong order: ((7+3)*1)*2 = 20. Therefore one student is rewarded 2 points: [20,13,42]
The points for the students are: [2,5,0]. The sum of the points is 2+5+0=7.

Example 2:
Input: s = "3+5*2", answers = [13,0,10,13,13,16,16]
Output: 19
Explanation: The correct answer of the expression is 13, therefore three students are rewarded 5 points each: [13,0,10,13,13,16,16]
A student might have applied the operators in this wrong order: ((3+5)*2 = 16. Therefore two students are rewarded 2 points: [13,0,10,13,13,16,16]
The points for the students are: [5,0,0,5,5,2,2]. The sum of the points is 5+0+0+5+5+2+2=19.

Example 3:
Input: s = "6+0*1", answers = [12,9,6,4,8,6]
Output: 10
Explanation: The correct answer of the expression is 6.
If a student had incorrectly done (6+0)*1, the answer would also be 6.
By the rules of grading, the students will still be rewarded 5 points (as they got the correct answer), not 2 points.
The points for the students are: [0,0,5,0,0,5]. The sum of the points is 10.

Example 4:
Input: s = "1+2*3+4", answers = [13,21,11,15]
Output: 11
Explanation: The correct answer of the expression is 11.
Every other student was rewarded 2 points because they could have applied the operators as follows:
- ((1+2)*3)+4 = 13
- (1+2)*(3+4) = 21
- 1+(2*(3+4)) = 15
The points for the students are: [2,2,5,2]. The sum of the points is 11.
 

Constraints:
3 <= s.length <= 31
s represents a valid expression that contains only digits 0-9, '+', and '*' only.
All the integer operands in the expression are in the inclusive range [0, 9].
1 <= The count of all operators ('+' and '*') in the math expression <= 15
Test data are generated such that the correct answer of the expression is in the range of [0, 1000].
n == answers.length
1 <= n <= 10^4
0 <= answers[i] <= 1000
"""

class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        def calculate(s: str) -> int:
            s = s + '+' # enable handle with last operator
            stack = [] # nums
            sign = '+' # previous sign
            cur_num = 0
            index = 0
            while index < len(s):
                if s[index] == ' ':
                    index += 1
                    continue
                if s[index].isdigit():
                    cur_num = cur_num * 10 + ord(s[index]) - ord('0')
                    index += 1
                    continue

                if sign == '+':
                    stack.append(cur_num)
                elif sign == '*':
                    stack.append(stack.pop() * cur_num)

                sign = s[index]
                cur_num = 0
                index += 1
            return sum(stack)

        def diffWaysToCompute(expression: str):
            # dfs or dfs + momo
            memo = {}
            def comp(s):
                if s in memo:
                    return memo[s]
                operators = ['+', '*']
                res = set()
                find_operator = False
                for i in range(len(s)):
                    if s[i] in operators:
                        find_operator = True
                        op = s[i]
                        left = s[:i]
                        right = s[i+1:]
                        left_res = comp(left)
                        right_res = comp(right)
                        for x in left_res:
                            for y in right_res:
                                if op == '+' and x+y<=1000:
                                    res.add(x+y)
                                elif op == '*' and x*y<=1000:
                                    res.add(x*y)
                if not find_operator:
                    res.add(int(s))
                memo[s] = res
                return res
            r = comp(expression)
            return r
        
        right_ans = calculate(s)
        partial_ans = diffWaysToCompute(s)
        
        ret = 0
        for ans in answers:
            if ans == right_ans:
                ret += 5
            elif ans in partial_ans:
                ret += 2
        return ret
 
 
