'''
275. H-Index II

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

(binary search)
'''
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # use binary search
        #left, right = 0, len(citations) - 1
        #while left < right:
        #    mid = (left + right) // 2

        h = 0
        for i in range(len(citations)):
            v = citations[len(citations) - i - 1]
            print(v, i, h, citations[len(citations) - i - 1])
            if v <= len(citations) - i - 1 and v > h:
                h = i + 1
        return h

if __name__ == '__main__':
    citations = [6, 5, 3, 0, 1]
    res = Solution().hIndex(citations)
    print(res)

