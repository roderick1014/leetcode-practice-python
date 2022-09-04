# 0133 - Clone Graph

'''
    Question:
        Given a reference of a node in a connected undirected graph.
        Reutrn a deep copy (clone) of the graph.
        Each node in the graph contains a value(int) and a list (List[Node]) of its neighbors.
'''

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:

    def cloneGraph(self, node):
        
        """
        :type: Node
        :rtype: Node
        """

        old2new = {}                                        # Initial a hashmap to record the nodes that has been traversed.
        
        def dfs(node):
            if node in old2new:                             # If the node is already existed and recorded in hashmap, return that node.
                return old2new[node]

            copy_node = Node(val = node.val)
            old2new[node] = copy_node

            for neighbor in node.neighbors:                 # Search each neighbor of the vertex.
                copy_node.neighbors.append(dfs(neighbor))   # Finish the cloning in recursive method.
            return copy_node

        return dfs(node) if node else None
        
if __name__ == '__main__':
    
    adjList = [[2,4],[1,3],[2,4],[1,3]]

    node_1 = Node(val = 1)
    node_2 = Node(val = 2)
    node_3 = Node(val = 3)
    node_4 = Node(val = 4)
    
    node_1.neighbors.append(node_2)
    node_1.neighbors.append(node_4)  
    
    node_2.neighbors.append(node_1)
    node_2.neighbors.append(node_3)

    node_3.neighbors.append(node_2)
    node_3.neighbors.append(node_4)

    node_4.neighbors.append(node_1)
    node_4.neighbors.append(node_3)
    
    sol = Solution()
    cloned = sol.cloneGraph(node_1)
    print(cloned.neighbors[1].neighbors[1].val)