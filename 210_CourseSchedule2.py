'''
210. Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
'''
import collections
class Solution(object):
    def findOrder_dfs(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
# need 2 way lookups: c -> p and p -> c
        graph = [[] for _ in range(numCourses)]
        neigh = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            graph[c].append(p)
            neigh[p].append(c)
        stack = [i for i in range(numCourses) if not graph[i]] # start
        res = []
        while stack:
            prerequisites = stack.pop()
            res.append(prerequisites)
            for course in neigh[prerequisites]:
                print(prerequisites, course)
                graph[course].remove(prerequisites)
                if not graph[course]: # when all courses removed
                    stack.append(course) # add to the process queue
        return res if len(res) == numCourses else [] # all courses in graph used or not

    def findOrder_bfs(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
# need 2 way lookups: c -> p and p -> c
        graph = [[] for _ in range(numCourses)]
        neigh = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            graph[c].append(p)
            neigh[p].append(c)
        queue = collections.deque([i for i in range(numCourses) if not graph[i]]) # start with course that has no prerequisites
        res = []
        while queue:
            prerequisites = queue.popleft()
            res.append(prerequisites)
            for course in neigh[prerequisites]:
                graph[course].remove(prerequisites)
                if not graph[course]: # when all courses removed
                    queue.append(course) # add to the process queue
        return res if len(res) == numCourses else []

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        def __directed_dfs(i):
            print("dfs:", visit[i])
            if visit[i] == 1: # valid order with no cycles
                return True
            if visit[i] == -1: # contain cycles
                return False
            visit[i] = -1 # default is not-valid
            for j in graph[i]: # all prerequisites
                if not __directed_dfs(j): # meet any prerequisites that returns false
                    return False
            visit[i] = 1
            print(i)
            res.append(i)
            return True

        graph = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            graph[c].append(p)
        print(graph)
        res = []
        visit = [0 for _ in range(numCourses)]
        print("visit:", visit)
        for i in range(numCourses):
            __directed_dfs(i)
            if not __directed_dfs(i):
                return []
        print("visit:", visit)
        return res

if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[0,1]]
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    res = Solution().findOrder_bfs(numCourses, prerequisites)
    print(res)
    res = Solution().findOrder_dfs(numCourses, prerequisites)
    print(res)
