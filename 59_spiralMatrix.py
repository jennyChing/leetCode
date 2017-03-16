'''
59. Spiral Matrix II

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Given n = 3,

You should return the following matrix:
[
[ 1, 2, 3 ],
[ 8, 9, 4 ],
[ 7, 6, 5 ]
]
'''
class Solution(object):
    def generateMatrix(self, n):
        # stimulate a person walking down the spiral
        res = [[0] * n for _ in range(n)]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] # right/down/left/up
        # i, j is the current location, d_indx is the direction for next step
        i, j, d_indx = 0, 0, 0

        # fill out the res matrix by walking down the spiral
        for v in range(1 , n * n + 1):
            res[i][j] = v
            # Decide which direction it is going next: (1) out of boundary or (2) reach visited entry
            print(v, i, j, res)
            if i + direction[d_indx][0] >= n or j + direction[d_indx][1] >= n or res[i + direction[d_indx][0]][j + direction[d_indx][1]] != 0 :
                d_indx = (d_indx + 1) % 4
            print(v, "Going next :", direction[d_indx])
            i += direction[d_indx][0]
            j += direction[d_indx][1]
        return res
if __name__ == "__main__":
    res = Solution().generateMatrix(3)
    print(res)


