"""
author: Wei Li
date: 10/20/2020

https://www.lintcode.com/problem/topological-sorting/description?_from=ladder&&fromId=161

127. Topological Sorting


Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

样例
挑战
Can you do it in both BFS and DFS?

说明
Learn more about representation of graphs

注意事项
You can assume that there is at least one topological order in the graph.
"""
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return None
        
       
        node_to_indegree = self.get_node_to_indegree(graph)
        
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        queue = collections.deque(start_nodes)
        
        order = []
        
        while queue:
            curr_node = queue.popleft()
            order.append(curr_node)
            
            for neighbor in curr_node.neighbors:
                node_to_indegree[neighbor] -= 1
                
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return order
    
    def get_node_to_indegree(self, graph):
        node_to_indegree = {n: 0 for n in graph}
        
        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1
        
        return node_to_indegree              