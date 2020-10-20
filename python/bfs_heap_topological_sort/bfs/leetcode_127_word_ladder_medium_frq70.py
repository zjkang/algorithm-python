"""
author: Wei Li
date: 10/20/2020

https://leetcode.com/problems/word-ladder/

127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord:
            return 0
        
        if endWord not in wordList:
            return 0
        
        
        queue = collections.deque([beginWord])
        visited = set([beginWord])
        
        distance = 0
        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return distance
                
                next_words = self.get_next_words(word)
               
                for next_word in next_words:
                    if next_word not in wordList or next_word in visited:
                        continue
                    
                    queue.append(next_word)
                    visited.add(next_word)
                
        
        return 0
    
    def get_next_words(self, curr):
        words = []
        
        for i in range(len(curr)):
            left, right = curr[:i], curr[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if curr[i] == char:
                    continue
                
                words.append(left + char + right)
        
        return words       