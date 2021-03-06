from heapq import heappush, heappop, heapreplace, heapify

class Solution(object):
    def kthSmallest(self, matrix, k):
        '''
        :type matrix: List[List[int]]
        :rtype: int
        binary search first locate row then column
        use heap to store sorted elements till kth, heapify function
        '''
        # row[0] is the first and smallest element in current row
        h = [(row[0], row, 1) for row in matrix] # next smallest, row number, col number
        print(h)
        # pop elements smaller then the kth element
        for _ in range(k - 1):
        # v is the current element of the row, r is the current row, i is the current column number
            v, r, i = h[0]
            # heapreplace: Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change.
            if i < len(r):
                heapreplace(h, (r[i], r, i + 1))
            else: # run out of elements on the current row, so pop it and move to next row
                heappop(h)
                print(h)
        return h[0][0] # always keep the kth smallest element here

# second attempt
    def kthSmallest(self, matrix, k):
        '''
        :type matrix: List[List[int]]
        :rtype: int
        binary search first locate row then column
        use heap to store sorted elements till kth, heapify function
        '''
	# idea for efficient solution: always keep 2 candidates in the min_heap, 1 is most right small, 1 is most down small
        min_heap = [(matrix[0][0], 0, 0)]
        while min_heap and k:
            k -= 1
            res, i, j = heapq.heappop(min_heap)
            if j == 0 and i + 1 < len(matrix):
                heapq.heappush(min_heap, (matrix[i + 1][j], i + 1, j)) # add cell below to the candidate list
            if j + 1 < len(matrix[0]):
                heapq.heappush(min_heap, (matrix[i][j + 1], i, j + 1)) # add cell right to the candidate list
        return res

if __name__ == '__main__':
    matrix = [[1, 5, 9], [10, 13, 13], [12, 13, 15]]
    matrix = [[-7, -5, -4, -4, -2, 90], [-1 ,1, 2, 3, 4, 96], [3, 5, 6, 7, 8, 100]]
    k = 10
    res = Solution().kthSmallest(matrix, k)
    print(res)


