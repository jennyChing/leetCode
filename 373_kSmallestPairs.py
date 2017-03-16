'''
373. Find K Pairs with Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
'''
from heapq import heappush, heappop, heapreplace, heapify

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums2 or not nums2:
            return []
        # use a heap to store all pairs' value
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        k = min(k, len(nums1) * len(nums2))
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heappush(h, (nums1[i] + nums2[j], i, j))
        res = []
        for _ in range(k):
            nextMin, i, j = heappop(h)
            res.append([nums1[i], nums2[j]])
        return res
# second attemp
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
# Sol1: 1-liner using heapq API:
        return heapq.nsmallest(k, ([n1, n2] for n1 in nums1 for n2 in nums2), key=sum)

# Sol2: heappop min_heap k times:
    def kSmallestPairs(self, nums1, nums2, k):
        if len(nums1)*len(nums2) <= k:
            return [[i, j] for i in nums1 for j in nums2]
        min_heap = [(n1 + n2, n1, n2) for n1 in nums1 for n2 in nums2]
        heapq.heapify(min_heap)
        pairs = []
        for i in range(k):
            pair_sum, n1, n2= heapq.heappop(min_heap)
            pairs.append([n1, n2])
        return pairs

#Sol3: Efficient way, heappush (i, j + 1) and (i + 1, j) to min_heap
    def kSmallestPairs(self, nums1, nums2, k):
        min_heap= []
        heapq.heappush(min_heap, [nums1[0] + nums2[0], 0, 0])
        pairs = []
        while min_heap and len(pairs) < k:
            _, i, j = heapq.heappop(min_heap)
            pairs.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2): # move right 1 col
                heapq.heappush(min_heap, [nums1[i] + nums2[j + 1], i, j + 1])
                print(i, j + 1)
            if j == 0 and i + 1 < len(nums1): # add cell below as candidate
                heapq.heappush(min_heap, [nums1[i + 1] + nums2[j], i + 1, j])
                print(i + 1, j)
            print(min_heap)
        return pairs

if __name__ == "__main__":
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    nums1 = [-10,-4,0,0,6]
    nums2 = [3,5,6,7,8,100]
    res = Solution().kSmallestPairs(nums1, nums2, 14)
    print(res)
