'''
274. H-Index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Hint:

*An easy approach is to sort the array first.
*What are the possible values of h-index?
*A faster approach is to use extra space.
'''
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        citations.sort()
        citations = citations[::-1]
        print(citations)
        for i, v in enumerate(citations):
            print(i, v, h)
            if v >= i + 1 and v > h:
                h = i + 1
        return h

# second attempt (without reverse, using len - i)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # idea: first sort the citations and increment h for i in citations: if len - i <= citations[i] and (i == 0 or citations[i - 1] <= len - i), h = len - i (need to check both sides!)
        citations = sorted(citations)
        n = len(citations)
        h = 0
        for i in range(n):
            if n - i <= citations[i] and (i == 0 or citations[i - 1] <= n - i): # n - i = i + 1
                h = n - i
        return h

if __name__ == '__main__':
    citations = [100]
    citations = [1, 2]
    res = Solution().hIndex(citations)
    print(res)
