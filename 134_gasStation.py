'''
134. Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
# recurive too complex! just need to record the valid start
        if sum(gas) < sum(cost):
            return -1 # not valid in any ways

        start, remain = 0, 0
        for i in range(len(gas)):
            remain += gas[i] - cost[i]
            print(remain, start)
            if remain < 0:
                remain = 0 # KEY: travel to the first one don't need gas, remain back to 0
                start = i + 1 # update start here (ask: how to ensure it is valid curcit?)
        return start

if __name__ == "__main__":
    gas, cost = [1,5,6], [4,2,1]
    gas, cost = [1,2],[2,1]
    gas, cost = [90,2,3,100], [100,1,90,1]
    gas, cost = [3,100,90,2], [90,1,103,1]
    res = Solution().canCompleteCircuit(gas, cost)
    print(res)

