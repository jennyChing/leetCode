'''
133. Clone Graph

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
'''
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        root = UndirectedGraphNode(node.label)
        print(root.label)
        stack = [node] # dfs record lasted visited nodes
        visited = {}
        visited[node.label] = root
        while stack:
            top = stack.pop()
            for n in top.neighbors:
                if n.label not in visited:
                    stack.append(n)
                    visited[n.label] = UndirectedGraphNode(n.label)
                visited[top.label].neighbors.append(visited[n.label])
        return root

if __name__ == "__main__":
    node0 = UndirectedGraphNode(0)
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    node0.neighbors.append(node1)
    node0.neighbors.append(node2)
    node1.neighbors.append(node0)
    node1.neighbors.append(node2)
    node2.neighbors.append(node0)
    node2.neighbors.append(node1)
    node2.neighbors.append(node2)
    res = Solution().cloneGraph(node0)
    while res:
        print(res.label)
        res = res.neighbors


