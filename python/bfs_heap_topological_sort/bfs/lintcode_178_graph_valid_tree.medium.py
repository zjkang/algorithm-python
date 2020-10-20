"""
author: Wei Li
date: 10/20/2020

https://www.lintcode.com/problem/graph-valid-tree/description?_from=ladder&&fromId=161

178. Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

样例
Example 1:

Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.
Example 2:

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
注意事项
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n - 1 != len(edges):
            return False
            
        graph= self.build_graph(n, edges)

        queue = collections.deque([0])
        visited = set([0])
        
        while queue:
            curr_node = queue.popleft()
            
            for neighbor in graph[curr_node]:
                if neighbor in visited:
                    continue
            
                visited.add(neighbor)
                queue.append(neighbor)
                    
            
        
        return len(visited) == n           
    
    def build_graph(self, n, edges):
        graph = [[] for _ in range(n)]
        
        for node_in, node_out in edges:
            graph[node_in].append(node_out)
            graph[node_out].append(node_in)

        
        return graph    