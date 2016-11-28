'''
332. Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.

Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
'''
import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d = collections.defaultdict(list)
        for t in tickets:
            d[t[0]] += [t[1]]
        # need to record visited cities? can transfer from other cities
        start = "JFK"
        res = []
        self.path = ["JFK"]
        def dfs(start):
            if len(self.path) == len(tickets) + 1: # check if valid path
                return self.path
            for stop in sorted(d[start]):
                d[start].remove(stop) # key: remove used stop to avoid infinite recursion
                self.path.append(stop)

                path = dfs(stop)
                if path: # check if any valid combination
                    return path # return to outter function call

                # Backtrack: undo the current path to last stage
                d[start] += stop,
                self.path.pop()

        return dfs(start)

if __name__ == "__main__":
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    res = Solution().findItinerary(tickets)
    print(res)
