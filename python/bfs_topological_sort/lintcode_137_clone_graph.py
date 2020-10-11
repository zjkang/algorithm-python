"""
author: Wei Li
date: 10/10/2020

https://www.lintcode.com/problem/clone-graph/description?_from=ladder&&fromId=161

137. clone graph

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Nodes are labeled uniquely.

You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.

样例
Example1

Input:
{1,2,4#2,1,4#4,1,2}
Output: 
{1,2,4#2,1,4#4,1,2}
Explanation:
1------2  
 \     |  
  \    |  
   \   |  
    \  |  
      4   
说明
How we serialize an undirected graph: http://www.lintcode.com/help/graph/

注意事项
You need return the node with the same label as the input node.


"""
"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return None
        
        # 1. find nodes
        nodes = self.find_nodes_by_bfs(node)
        
        # 2. copy nodes
        mapping = self.copy_nodes(nodes)
        
        # 3. copy edges
        self.copy_edges(nodes, mapping)
        
        return mapping[node]
    
    def find_nodes_by_bfs(self, node):
        queue = collections.deque([node])
        visited = set([node])
        
        while queue:
            curr_node = queue.popleft()
            
            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return visited
        
    def copy_nodes(self, nodes):
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        
        return mapping
    
    
    def copy_edges(self, nodes, mapping):
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)