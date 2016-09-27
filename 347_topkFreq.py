import operator
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        memo = {}
        for n in nums:
            if n in memo:
                memo[n] += 1
            else:
                memo[n] = 1
        #sorted_freq = sorted(memo.items(), key=operator.itemgetter(1), reverse = True)
        sorted_freq = [k for v, k in sorted([(v, k) for k, v in memo.items()], reverse = True)]
        print(sorted([(v, k) for k, v in memo.items()], reverse = True))
        return sorted_freq[:k]
if __name__ == '__main__':
    res = Solution().topKFrequent([5,5,5,4,4,3], 2)
    print(res)
