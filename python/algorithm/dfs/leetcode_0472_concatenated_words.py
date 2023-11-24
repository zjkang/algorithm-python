'''
author: Zhengjian Kang
date: 04/27/2021

残酷群每日一题: 04/27/2021

https://leetcode.com/problems/concatenated-words/

472. Concatenated Words

note: dfs + trie + memo

Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least
two shorter words in the given array.

Example 1:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:
Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
 

Constraints:
1 <= words.length <= 10^4
0 <= words[i].length <= 1000
words[i] consists of only lowercase English letters.
0 <= sum(words[i].length) <= 6 * 10^5
'''

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

def add_word(root, word):
    for i in range(len(word)):
        if word[i] not in root.children:
            root.children[word[i]] = TrieNode()
        root = root.children[word[i]]
        if i == len(word) - 1:
            root.is_word = True

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if len(words) <= 2: return []
        words.sort(key=lambda x: len(x))
        n = len(words)
        
        root = TrieNode()
        add_word(root, words[0])
        
        res = []
        for i in range(1, n):
            if self.dfs(words[i], 0, root, {}):
                res.append(words[i])
            add_word(root, words[i])
        return res
        
    def dfs(self, word, index, root, memo):
        if index in memo: return memo[index]
        if index == len(word):
            memo[index] = True
            return memo[index]
        cur = root
        for i in range(index, len(word)):
            if word[i] not in cur.children:
                memo[index] = False
                return memo[index]
            
            cur = cur.children[word[i]]
            if cur.is_word:
                if self.dfs(word, i+1, root, memo):
                    memo[index] = True
                    return memo[index]
        memo[index] = False
        return memo[index]
