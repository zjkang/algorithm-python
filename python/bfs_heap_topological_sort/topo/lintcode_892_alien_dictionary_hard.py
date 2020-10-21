"""
author: Wei Li
date: 10/20/2020

https://www.lintcode.com/problem/alien-dictionary/note/229404

892. Alien Dictionary


There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

样例
Example 1:
Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"

Example 2:
Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"

注意事项
You may assume all letters are in lowercase.
The dictionary is invalid, if a is prefix of b and b is appear before a.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in normal lexicographical order
"""
import heapq
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        if not words:
            return ""
        
        graph = self.buildGraph(words)
       
        if not graph:
            return ""
           
        indegres = self.getIndegres(graph)
        
        queue = [node for node in graph if indegres[node] == 0]
        
        heapq.heapify(queue)
      
        ans = ""
        while queue:
            node = heapq.heappop(queue)
            ans += node
            
            for neigbor in graph[node]:
                indegres[neigbor] -= 1
                
                if indegres[neigbor] == 0:
                    heapq.heappush(queue, neigbor)
        
        if len(ans) == len(indegres):
            return ans
            
        return ""        
    
    def getIndegres(self, graph):
        indegres = {node: 0 for node in graph}
        
        for n in graph:
            for neigbor in graph[n]:
                indegres[neigbor] += 1
        
        return indegres        
    
    def buildGraph(self, words):
        graph = {}
        
        # add the nodes to graph
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()
        
        
        # add the edges
        n = len(words)
        
        for i in range(n - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break
    
            
        return graph        
    
    
        