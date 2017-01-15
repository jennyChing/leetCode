'''
399. Evaluate Division

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
'''
import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
# built graph with dict of dict and calculate the values
        graph = collections.defaultdict(dict)
        for e, v in zip(equations, values):
            graph[e[0]][e[1]], graph[e[1]][e[0]] = v, 1.0 / v
            graph[e[0]][e[0]], graph[e[1]][e[1]] = 1.0, 1.0

        for k in graph: # the middle guy
            for i in graph: # if i can reach j through k
                for j in graph: # (i to j) = (i to k) * (k to j)
                    if k in graph[i] and j in graph[k]:
                        graph[i][j] = graph[i][k] * graph[k][j]
        res = []
        for q in queries: # lookup graph updated with kij algorithm
            if q[1] not in graph[q[0]]:
                res.append(-1)
            else:
                res.append(graph[q[0]][q[1]])
        return res

if __name__ == "__main__":
    equations = [ ["a", "b"], ["b", "c"] ]
    values = [2.0, 3.0]
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
    res = Solution().calcEquation(equations, values, queries)
    print(res)
