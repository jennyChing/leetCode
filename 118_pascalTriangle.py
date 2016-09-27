'''
118. Pascal's Triangle

Given numRows, generate the first numRows of Pascal's triangle.
Dynamic programming
'''
class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return [1]
        result = []
        for i in range(numRows):
            result.append([]) # add a new row
            for j in range(i + 1):
                result[i].append(1 if j in (0, i) else result[i - 1][j - 1] + result[i - 1][j]) # the first and last of each row is 1, others are the sum of the two above it
        print(result, numRows)
        return result[numRows]
if __name__ == '__main__':
    assert Solution().generate(4) == [1,4,6,4,1]
    assert Solution().generate(0) == [1]


