from heapq import heappush, heappop, heapreplace, heapify

class Solution(object):
    def kthSmallest(self, matrix, k):
        '''
        :type matrix: List[List[int]]
        :rtype: int
        binary search first locate row then column
        use heap to store sorted elements till kth, heapify function
        '''
        h = [(row[0], row, 1) for row in matrix]
        # pop elements smaller then the kth element
        for _ in range(k - 1):
        # v is the current element of the row, r is the remaining row, i is the current column number
            v, r, i = h[0]
            # heapreplace: Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change.
            if i < len(r):
                heapreplace(h, (r[i], r, i + 1))
                print(h)
            else:
                heappop(h)
                print(h)
        return h[0][0]

if __name__ == '__main__':
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    Solution().kthSmallest(matrix, k)


