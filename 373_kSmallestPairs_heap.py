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
        if not nums1 or not nums2: return []
# Step1: combine nums1 and nums2 into a matrix with all the combinations (then similiart to #378 - search kth smallest element in matrix!
        matrix = []
        for i in range(len(nums1)):
            row = []
            for j in range(len(nums2)):
                row.append(nums1[i] + nums2[j]) # compute the pair sum
            matrix.append(row)
# Step2: traverse the graph and find the kth smallest element
    # current smallest, complete list, and the position of the current smallest in the list
        h = [(row[0], row, 1, ) for row in matrix] # next smallest, row number, col number
        # pop elements smaller then the kth element
        for _ in range(k - 1):
        # v is the current element of the row, r is the current row, i is the current count
            v, r, i = h[0]
            # heapreplace: Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change.
            if i < len(r): # check elements left in current row
                heapreplace(h, (r[i], r, i + 1))
            elif len(h) > 1: # check enough rows left to pop
                # run out of elements on the current row, so pop it and move to next row
                heappop(h)
            else:
                break
        cols = [h[i][2] for i in range(len(h))]
        i_range, j_range = len(matrix) - len(h) + 1, h[0][2]
        pairs = []
        for i in range(i_range):
            for j in range(j_range):
                pairs.append([nums1[i], nums2[j]])
        return pairs


if __name__ == "__main__":
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    res = Solution().kSmallestPairs(nums1, nums2, 2)
    print(res)
