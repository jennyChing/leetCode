'''
310. Minimum Height Trees

For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]
'''

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
# Similar idea from UVA #10459, without index/node off-by-one problem with both zero-based index

        def __directed_dfs(position, parent, dep, visited):
            for node in tree[position]:
                visited.add(position)
                if node != position and node not in visited:
                    # increase the neighbor's depth by 1 (node - 1 will be the position):
                    dep[node] = dep[position] + 1
                    __directed_dfs(node, position, dep, visited)

        tree = [[] for _ in range(n)]
        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])
        min_dep = float('inf')
        dep_all = [] * n
        for i in range(n): # use i as root for the tree
            dep = [1] * n
            __directed_dfs(i, i, dep, visited=set()) # start with root: root's parent is root itself
            dep_all.append(dep)
            min_dep = min(max(dep), min_dep)
        res = []
        for r in range(n):
            if max(dep_all[r]) == min_dep:
                res.append(r)
        return res

if __name__ == "__main__":
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    res = Solution().findMinHeightTrees(6, edges)
    print(res)
