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

	# Use at most the first k of each, then get the sizes.
        nums1 = nums1[:k]
        nums2 = nums2[:k]
        m, n = len(nums1), len(nums2)

# Step1: combine nums1 and nums2 into a matrix with all the combinations (then similiart to #378 - search kth smallest element in matrix!
        matrix = []
        for i in range(len(nums1)):
            row = []
            for j in range(len(nums2)):
                row.append(nums1[i] + nums2[j]) # compute the pair sum
            matrix.append(row)

# Step2: traverse the graph and find the kth smallest element value (kthSum)
    # current smallest, complete list, and the position of the current smallest in the list
        pairs = {(nums1[0], nums2[0])}
        h = [(row[0], v, i, 0) for i, v in enumerate(matrix)] # next smallest, row, row number, col number
        # pop elements smaller then the kth element
        for _ in range(k - 1):
            print(h)
        # v is the current element of the row, r is the current row, i is the current count
            v, r, i, j = h[0]
            if i < len(r): # check elements left in current row
                print("pairSum:", matrix[i][j], i, j)
                print()
                heapreplace(h, (r[j], r, i, j + 1))
            elif len(h) > 1: # check enough rows left to pop
                # run out of elements on the current row, so pop it and move to next row
                heappop(h)
            else:
                break
        kthSum = h[0][0]
        print(pairs)
        print(h)

# Collect all pairs with sum smaller than kthSum as well as k pairs whose sum equals kthSum.
        pairs = []
        for a in nums1:
            for b in nums2:
                if a + b <= kthSum:
                    pairs.append([a, b])
        return pairs


if __name__ == "__main__":
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    nums1 = [0,0,0]
    nums2 = [-3,22,35]
    res = Solution().kSmallestPairs(nums1, nums2, 9)
    print(res)
