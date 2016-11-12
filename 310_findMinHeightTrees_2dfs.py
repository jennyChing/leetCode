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
# Optimize: only need to call the dfs twice instead of n times to find the tree diameter

        def __directed_dfs(position, visited):
            longest_path = []
            for node in tree[position]:
                visited.add(position)
                if node not in visited:
                    path = __directed_dfs(node, visited)
                    if len(path) > len(longest_path):
                        longest_path = path
            longest_path.append(position)
            return longest_path

        tree = [[] for _ in range(n)]
        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])
        path = __directed_dfs(0, set())
        diameter = __directed_dfs(path[0], set())
        print(diameter)
        mid = len(diameter) >> 1

        return [path[mid]] if len(diameter) % 2 else sorted(diameter[mid - 1:mid + 1])

if __name__ == "__main__":
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    edges = [[0,1],[0,2]]
    res = Solution().findMinHeightTrees(3, edges)
    print(res)
