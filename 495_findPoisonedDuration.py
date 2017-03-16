'''
495. Teemo Attacking

In LLP world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.
'''
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = len(timeSeries) * duration
        for i in range(1, len(timeSeries)):
            overlap = 0 if timeSeries[i] > timeSeries[i - 1] + duration else timeSeries[i - 1] + duration - timeSeries[i]
            res -= overlap
        return res

if __name__ == '__main__':
    res = Solution().findPoisonedDuration([1,2], 2)
    print(res)

